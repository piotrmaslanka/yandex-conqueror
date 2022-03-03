DROP KEYSPACE IF EXISTS yandex;


CREATE KEYSPACE IF NOT EXISTS yandex WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};


CREATE TABLE yandex.accounts (
    email TEXT,
    password TEXT,
    status INT, -- 0 - active, 1 - suspended
    PRIMARY KEY (email)
);
