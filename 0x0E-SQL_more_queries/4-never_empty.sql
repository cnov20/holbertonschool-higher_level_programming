-- Creates a table if it does not exist and id field default value
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256) NOT NULL);
