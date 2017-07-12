-- Creates a table if doesn't exist and field unique, default value
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
