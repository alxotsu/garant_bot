import sqlite3
import telebot
from config import QIWI_TOKEN, REPLENISH, QIWI_ID, DATABASE, BOT_TOKEN
import random
import requests


def first_join(user_id, username):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q = q.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
    row = q.fetchone()
    connection.close()
    if row is None:
        q.execute(
            f"INSERT INTO users (user_id, offers, balance, qiwi, ban, nick) VALUES ('{user_id}', '0', '0', 'Не указан', '0', '{username}')"
        )
        connection.commit()


def check_ban(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q = q.execute(f"SELECT ban FROM users WHERE user_id = '{user_id}'")
    results = q.fetchone()
    connection.close()
    return results


def profile(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    results = q.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'").fetchone()
    connection.close()
    return results


def last_offers_seller(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    row = q.execute(
        f"SELECT act FROM last_offers WHERE seller = '{user_id}'"
    ).fetchall()
    connection.close()
    text = ""
    for i in row:
        text = text + "💠 " + i[0] + "\n\n"
    return text


def last_offers_customer(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    row = q.execute(
        f"SELECT act FROM last_offers WHERE customer = '{user_id}'"
    ).fetchall()
    connection.close()
    text = ""
    for i in row:
        text = text + "💠 " + i[0] + "\n\n"
    return text


def write_qiwi(user_id, qiwi_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q.execute(f"UPDATE users SET qiwi = ('{qiwi_id}') WHERE user_id = '{user_id}'")
    connection.commit()
    connection.close()


def output_qiwi(user_id, balance, money):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    ost = float(balance) - float(money)
    q.execute(f"UPDATE users SET balance = ('{ost}') WHERE user_id = '{user_id}'")
    connection.commit()
    connection.close()


def ban(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    try:
        q.execute(f"UPDATE users SET ban = '1' WHERE user_id = '{user_id}'")
    except:
        pass
    connection.commit()
    connection.close()


def unban(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    try:
        q.execute(f"UPDATE users SET ban = '0' WHERE user_id = '{user_id}'")
    except:
        pass
    connection.commit()
    connection.close()


def edit_balance(balance, user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    try:
        q.execute(f"UPDATE users SET balance = '{balance}' WHERE user_id = '{user_id}'")
    except:
        pass
    connection.commit()
    connection.close()


def check_payment(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        params = {"rows": "5"}
        headers = {"authorization": f"Bearer {QIWI_TOKEN}"}
        resp = requests.get(
            f"https://edge.qiwi.com/payment-history/v1/persons/{QIWI_ID}/payments",
            params=params,
            headers=headers,
        ).json()

        check_payment_obj = cursor.execute(
            f"SELECT * FROM check_payment WHERE user_id = {user_id}"
        ).fetchone()
        comment = check_payment_obj[1]

        for data_obj in resp["data"]:
            if (
                str(comment) in data_obj["comment"]
                and "643" in data_obj["sum"]["currency"]
            ):
                info = profile(user_id)
                balance = float(info[2]) + float(data_obj["sum"]["amount"])
                cursor.execute(
                    f"UPDATE users SET balance = '{balance}' WHERE user_id = '{user_id}'"
                )
                conn.commit()
                cursor.execute(f"DELETE FROM check_payment WHERE user_id = '{user_id}'")
                conn.commit()
                return data_obj["sum"]["amount"]
    except Exception as e:
        print(e)
    conn.close()


def canel_payment(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM check_payment WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def replenish_balance(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    code = "".join(random.choice("0123456789") for _ in range(6))

    cursor.execute(f"INSERT INTO check_payment VALUES ('{user_id}', '{code}')")
    conn.commit()
    conn.close()
    msg = REPLENISH.format(
        code=code,
    )
    return msg, code


def admin_message():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"SELECT user_id FROM users")
    row = cursor.fetchall()
    conn.close()
    return row


def search(search_line):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    row = q.execute(
        f"SELECT * FROM users WHERE user_id = '{search_line}' OR nick = '{search_line}'"
    ).fetchone()
    connection.close()
    return row


def deal(seller_id, customer_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q.execute(
        f"INSERT INTO temp_deal (user_id, user_id2, status) VALUES ('{seller_id}', '{customer_id}', 'dont_open')"
    )
    connection.commit()
    connection.close()


def delete_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM temp_deal WHERE user_id2 = '{user_id}'")
    conn.commit()
    conn.close()


def delete_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM temp_deal WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def info_deal_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT user_id FROM temp_deal WHERE user_id2 = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def info_deal_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT user_id2 FROM temp_deal WHERE user_id = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def search_block(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    row = q.execute(
        f"SELECT * FROM temp_deal WHERE user_id = '{user_id}' OR user_id2 = '{user_id}'"
    ).fetchone()
    connection.close()
    return row


def stats():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(f"SELECT user_id FROM users").fetchone()
    amount_user_all = 0
    while row is not None:
        amount_user_all += 1
        row = cursor.fetchone()

    row = cursor.execute(f"SELECT act FROM last_offers").fetchone()
    amount_offers_all = 0
    while row is not None:
        amount_offers_all += 1
        row = cursor.fetchone()

    conn.close()
    msg = (
        "❕ Информация:\n\n❕ Пользователей в боте - "
        + str(amount_user_all)
        + "\n❕ Проведено сделок - "
        + str(amount_offers_all)
    )
    return msg


def info_offer_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT status FROM temp_deal WHERE user_id2 = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def info_offer_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT status FROM temp_deal WHERE user_id = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def accept_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE temp_deal SET status = 'open' WHERE user_id2 = '{user_id}'")
    conn.commit()
    conn.close()


def accept_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE temp_deal SET status = 'open' WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def info_offers_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT * FROM temp_deal WHERE user_id = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def info_offers_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    row = cursor.execute(
        f"SELECT * FROM temp_deal WHERE user_id2 = '{user_id}'"
    ).fetchone()
    conn.close()
    return row


def edit_price(price, user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE temp_deal SET sum = ('{price}') WHERE user_id = '{user_id}'"
    )
    conn.commit()
    conn.close()


def success(user_id, balance):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE temp_deal SET status = 'success' WHERE user_id2 = '{user_id}'"
    )
    conn.commit()
    cursor.execute(
        f"UPDATE users SET balance = ('{balance}') WHERE user_id = '{user_id}'"
    )
    conn.commit()
    conn.close()


def yes_cancel_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM temp_deal WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def yes_cancel_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM temp_deal WHERE user_id2 = '{user_id}'")
    conn.commit()
    conn.close()


def ok(
    customer_id,
    seller_id,
    amount,
    num,
    seller_amount,
    seller_username,
    customer_username,
    seller_offers,
    customer_offers,
):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    balance = float(seller_amount) + float(amount)
    cursor.execute(
        f"UPDATE users SET balance = ('{balance}') WHERE user_id = '{seller_id}'"
    )
    cursor.execute(
        f"UPDATE users SET offers = ('{int(seller_offers) + 1}') WHERE user_id = '{seller_id}'"
    )
    cursor.execute(
        f"UPDATE users SET offers = ('{int(customer_offers) + 1}') WHERE user_id = '{customer_id}'"
    )
    cursor.execute(
        f"INSERT INTO last_offers (customer, seller, act) VALUES ('%s', '%s', '%s')"
        % (
            customer_id,
            seller_id,
            "Продавец(ID - "
            + str(seller_id)
            + ")(@"
            + str(seller_username)
            + ") провёл успешную сделку №"
            + str(num)
            + " на сумму "
            + str(amount)
            + " рублей с покупателем(ID - "
            + str(customer_id)
            + ")(@"
            + str(customer_username)
            + ")",
        )
    )
    cursor.execute(
        f"UPDATE temp_deal SET status = ('review') WHERE user_id2 = '{customer_id}'"
    )
    conn.commit()
    conn.close()


def dispute_customer(chat_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE temp_deal SET status = ('dispute') WHERE user_id2 = '{chat_id}'"
    )
    conn.commit()
    conn.close()


def dispute_seller(chat_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE temp_deal SET status = ('dispute') WHERE user_id = '{chat_id}'"
    )
    conn.commit()
    conn.close()


def dispute_info(user_id):
    conn = sqlite3.connect(DATABASE)
    q = conn.cursor()
    row = q.execute(f"SELECT * FROM temp_deal WHERE id_offer = '{user_id}'")
    row = row.fetchone()
    conn.close()
    return row


def deal_true(offer_id, user_id, amount_customer, amount_offer):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    balance_customer = float(amount_customer) + float(amount_offer)
    cursor.execute(
        f"UPDATE users SET balance = ('{balance_customer}') WHERE user_id = '{user_id}'"
    )
    cursor.execute(f"DELETE FROM temp_deal WHERE id_offer = '{offer_id}'")
    conn.commit()
    conn.close()


def dispute_info_customer(user_id):
    conn = sqlite3.connect(DATABASE)
    q = conn.cursor()
    row = q.execute(f"SELECT * FROM temp_deal WHERE user_id2 = '{user_id}'")
    row = row.fetchone()
    conn.close()
    return row


def dispute_info_seller(user_id):
    conn = sqlite3.connect(DATABASE)
    q = conn.cursor()
    row = q.execute(f"SELECT * FROM temp_deal WHERE user_id = '{user_id}'")
    row = row.fetchone()
    conn.close()
    return row


def check_deal(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    result = q.execute(f"SELECT user_id FROM users WHERE nick = '{user_id}'").fetchone()
    row = q.execute(
        f"SELECT user_id2 FROM temp_deal WHERE user_id = '{result[0]}'"
    ).fetchone()
    if row is None:
        row = q.execute(
            f"SELECT user_id FROM temp_deal WHERE user_id2 = '{result[0]}'"
        ).fetchone()
    connection.close()
    return row


def up_login(username, user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    result = q.execute(
        f"SELECT user_id FROM users WHERE nick = '{username}'"
    ).fetchone()
    if result is None:
        q.execute(f"UPDATE users SET nick = ('{username}') WHERE user_id = '{user_id}'")
        connection.commit()
    connection.close()
    return result


def cancel_open_offer(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    result = q.execute(
        f"SELECT * FROM temp_deal WHERE user_id2 = '{user_id}' OR user_id = '{user_id}'"
    ).fetchone()
    connection.close()
    if result[4] == "dont_open":
        q.execute(
            f"DELETE FROM temp_deal WHERE user_id2 = '{user_id}' OR user_id = '{user_id}'"
        )
        connection.commit()
        return True, result[0]
    else:
        return False, None


def reviews(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    row = q.execute(f"SELECT review FROM reviews WHERE seller = '{user_id}'").fetchall()
    text = ""
    for i in row:
        text = text + "💠 " + i[0] + "\n\n"
    connection.close()
    return text


def close_offer(user_id):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q.execute(
        f"DELETE FROM temp_deal WHERE user_id2 = '{user_id}' OR user_id = '{user_id}'"
    )
    connection.commit()
    connection.close()


def add_review(seller_id, sums, customer_id, review):
    connection = sqlite3.connect(DATABASE)
    q = connection.cursor()
    q.execute(
        "INSERT INTO reviews (seller, sum, customer, review) VALUES ('%s', '%s', '%s', '%s')"
        % (seller_id, sums, customer_id, review)
    )
    connection.commit()
    connection.close()
