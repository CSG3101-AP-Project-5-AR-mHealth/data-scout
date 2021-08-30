CREATE DATABASE vitalsdb;
USE vitalsdb;
DROP TABLE IF EXISTS vitals;
CREATE TABLE vitals
(
    id int(11) NOT NULL,
    heart_rate int(11) NOT NULL,
    body_temp int(11) NOT NULL,
    eventTime timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
);

SHOW TABLES;