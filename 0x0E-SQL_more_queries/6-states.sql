-- Creates a db and table if doesn't exist and field unique, default value, pk
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT NOT NULL AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id)
);
