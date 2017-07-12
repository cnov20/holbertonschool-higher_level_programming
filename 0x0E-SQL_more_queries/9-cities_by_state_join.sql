-- Script lists all cities contained in a given database
-- via join method
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states;
