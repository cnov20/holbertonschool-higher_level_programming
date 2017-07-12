-- Script lists all cities in cities table when referencing states table
-- Via subquery
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California');
