-- Script lists all records contained in a given database
-- via join method
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name  ASC;
