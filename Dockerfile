FROM python:3.9 AS runtime

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# todo: remove for production release
RUN pip install coverage nose2 wait-for-cassandra
WORKDIR /app

ADD conqueror /app/conqueror

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "conqueror.app:app"]

FROM runtime AS unittest



ENV DEBUG=1 CI=1

ADD tests /app/tests
RUN chmod ugo+x /app/tests/test.sh
CMD ["/app/tests/test.sh"]