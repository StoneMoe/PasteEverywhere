# syntax=docker/dockerfile:experimental
FROM python:3.10-bullseye
WORKDIR /app

COPY ./server/requirements.txt ./
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

COPY ./server/ .
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
