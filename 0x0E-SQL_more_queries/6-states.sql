-- Creates a db and table if doesn't exist and field unique, default value, pk
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states.htbn_0d_usa (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);
