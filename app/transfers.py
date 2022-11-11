from decimal import Decimal
from datetime import datetime

from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from tronpy import Tron
from tronpy.keys import PrivateKey
import requests
from app import config
from models import queries


def get_royalty(withdrawal):
    if withdrawal.amount < 1000:
        tax = 0.02
        minimum = 2
    else:
        tax = 0.01
        minimum = 20

    if withdrawal.user.referral_id:
        tax = tax * (1 - config.REFERRAL_TAX_SALE / 100)

    royalty = withdrawal.amount * Decimal(str(tax))
    royalty = max(minimum, royalty)

    return royalty


def check_binance_usdt_transaction(trans_hash, user):
    if queries.get_transaction(trans_hash) is not None:
        return "this_transaction_already_registered"

    web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.default_account = config.SYSTEM_WALLET_ADDRESS

    try:
        transaction = web3.eth.get_transaction(bytes.fromhex(trans_hash))
    except TransactionNotFound:
        return "transaction_not_found"

    abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]

    addr = web3.toChecksumAddress("0x184BD594a5f06ABb86c75dFcCa588071dc11d6D0")
    contract = web3.eth.contract(address=addr, abi=abi)
    transaction_info = contract.decode_function_input(transaction.input)[1]

    if transaction_info["to"] != config.SYSTEM_WALLET_ADDRESS:
        return "incorrect_recipient"

    amount = Decimal(str(transaction_info["value"] / 10**18))
    transaction = queries.new_transaction(trans_hash, user.chat_id, amount)
    user.balance += amount
    user.save()
    return transaction


def check_binance_usdt_system_balance():
    web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.default_account = config.SYSTEM_WALLET_ADDRESS

    abi = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "type": "function",
        }
    ]

    addr = web3.toChecksumAddress("0x184BD594a5f06ABb86c75dFcCa588071dc11d6D0")
    contract = web3.eth.contract(address=addr, abi=abi)

    balance = contract.functions.balanceOf(config.SYSTEM_WALLET_ADDRESS).call()

    return Decimal(balance) / 10**18


def process_binance_usdt_withdrawal(withdrawal):
    assert withdrawal.amount < check_binance_usdt_system_balance()

    web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.default_account = config.SYSTEM_WALLET_ADDRESS

    abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "_to", "type": "address"},
                {"name": "_value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]

    addr = web3.toChecksumAddress("0x184BD594a5f06ABb86c75dFcCa588071dc11d6D0")
    contract = web3.eth.contract(address=addr, abi=abi)

    amount = int(get_royalty(withdrawal) * 10 ** 18)

    transfer = contract.functions.transfer(
        withdrawal.blockchain_address, amount
    ).buildTransaction(
        {
            "chainId": 56,
            "gas": config.OUTPUT_GAS_COUNT,
            "gasPrice": web3.eth.gasPrice,
            "nonce": web3.eth.getTransactionCount(config.SYSTEM_WALLET_ADDRESS),
        }
    )
    account = web3.eth.account.privateKeyToAccount(config.SYSTEM_WALLET_PRIVATE_KEY)
    signed_transfer = account.signTransaction(transfer)
    sent_transfer = web3.eth.sendRawTransaction(signed_transfer.rawTransaction)

    withdrawal.passed = True
    withdrawal.close_time = datetime.utcnow()
    withdrawal.save()

    return sent_transfer.hex()


def check_trc20_usdt_transaction(trans_hash, user):
    if queries.get_transaction(trans_hash) is not None:
        return "this_transaction_already_registered"

    transaction_info = requests.get(
        'https://apilist.tronscanapi.com/api/transaction-info',
        params={'hash': trans_hash},
    ).json()
    if not transaction_info:
        return "transaction_not_found"

    address = transaction_info['tokenTransferInfo']['to_address']

    if address != config.SYSTEM_WALLET_ADDRESS:
        return "incorrect_recipient"

    amount = Decimal(transaction_info['tokenTransferInfo']['amount_str']) / 10**6
    transaction = queries.new_transaction(trans_hash, user.chat_id, amount)
    user.balance += amount
    user.save()
    return transaction


def check_trc20_usdt_system_balance():
    wallet_info = requests.get(
        'https://apilist.tronscanapi.com/api/account/tokens',
        params={'address': config.SYSTEM_WALLET_ADDRESS},
    ).json()
    if 'data' not in wallet_info:
        raise Exception("Bad wallet address.")

    for token in wallet_info['data']:
        if token['tokenId'] == 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t':
            return Decimal(str(token['quantity']))
    return 0


def process_trc20_usdt_withdrawal(withdrawal):
    #assert withdrawal.amount < check_trc20_usdt_system_balance()

    client = Tron()
    contract = client.get_contract('TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t')

    amount = (withdrawal.amount - get_royalty(withdrawal)) * 10 ** 6
    txn = (
        contract.functions.transfer(withdrawal.blockchain_address, int(amount))
        .with_owner(config.SYSTEM_WALLET_ADDRESS)
        .fee_limit(config.OUTPUT_GAS_COUNT)
        .build()
        .sign(PrivateKey(bytes.fromhex(config.SYSTEM_WALLET_PRIVATE_KEY)))
    )

    txn = txn.broadcast()
    transaction_info = {}
    while 'contractRet' not in transaction_info:
        try:
            transaction_info = requests.get(
                'https://apilist.tronscanapi.com/api/transaction-info',
                params={'hash': txn.txid},
            ).json()
        except:
            pass
    res = transaction_info['contractRet'] == 'SUCCESS'
    if not res:
        raise Exception(transaction_info['contractRet'])

    return txn.txid
