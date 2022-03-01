FROM python:3.9

WORKDIR /app

ADD conqueror /app/conqueror

RUN python -m conqueror
