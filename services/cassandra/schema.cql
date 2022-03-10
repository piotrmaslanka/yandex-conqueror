DROP KEYSPACE IF EXISTS yandex;


CREATE KEYSPACE IF NOT EXISTS yandex WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};


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


CREATE TABLE yandex.review_count (
    apiKey  TEXT,
    count INT,
    PRIMARY KEY (apiKey)
);

