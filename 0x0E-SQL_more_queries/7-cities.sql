-- Creates a db and table if doesn't exist and field unique, NOT NULL, AUTO INCR
-- PRIMARY KEY AND FOREIGN KEY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states (id)
);
