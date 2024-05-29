FROM python:3.11.1-slim-buster as base
ENV WEBHOOK_APP_NAME=api

WORKDIR /usr/src/app/$WEBHOOK_APP_NAME

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

ADD pyproject.toml /usr/src/app/$WEBHOOK_APP_NAME

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /usr/src/app/$WEBHOOK_APP_NAME