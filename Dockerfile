FROM python:3.10

WORKDIR /bot

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    pip install --upgrade setuptools \
    pip install -r requirements.txt

COPY . .