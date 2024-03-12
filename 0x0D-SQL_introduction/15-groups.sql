-- Script that lists records with same score numbers from first_table
SELECT score, COUNT(*) AS numberi FROM second_table GROUP BY score ORDER BY number DESC;
