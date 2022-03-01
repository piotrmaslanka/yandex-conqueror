FROM python:3.9

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

ADD conqueror /app/conqueror

RUN python -m conqueror
