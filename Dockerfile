# Base target.
FROM python:3.10.3-alpine AS base

ARG BUILD_NUMBER

ENV BUILD_NUMBER=$BUILD_NUMBER
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install pipenv

COPY Pipfile* ./

# Dev target.
FROM base AS dev

RUN pipenv install --system --deploy --dev

COPY config.py ./config.py
COPY main.py ./main.py
COPY app ./app

# Test target.
FROM dev AS test

COPY tests ./tests

# Release target.
FROM base AS release

RUN pipenv install --system --deploy

COPY config.py ./config.py
COPY main.py ./main.py
COPY app ./app

CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app
