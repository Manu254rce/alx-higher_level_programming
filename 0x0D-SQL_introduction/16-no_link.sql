-- Script that lists al records of the table of the DB
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
