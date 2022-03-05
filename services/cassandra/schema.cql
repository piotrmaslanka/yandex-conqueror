DROP KEYSPACE IF EXISTS yandex;


CREATE KEYSPACE IF NOT EXISTS yandex WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};


CREATE TABLE yandex.accounts (
    email TEXT,
    password TEXT,
    status INT, -- 0 - active, 1 - suspended
    PRIMARY KEY (email)
);


CREATE TABLE yandex.sectors (
    sector TEXT,
    PRIMARY KEY (sector)
);

CREATE TABLE yandex.businesses (
    sector      TEXT,               -- sector, as defined before
    businessID TEXT,                -- yandex business ID
    reqId      TEXT,                -- request ID, gained through Yandex searches
    geoLat      FLOAT,          -- geo latitude in degrees, + is North
    geoLon      FLOAT,          -- geo longitude in degrees. + is East
    name        TEXT,           -- text name
    PRIMARY KEY (sector, businessID)
);


CREATE TABLE yandex.entries (
    apiKey  TEXT,
    entries INT,
    PRIMARY KEY (apiKey);
);

