-- Script that rturns the max temp from a SQL dump
SOURCE temperatures.sql

SELECT state, MAX(temperature) AS max_temperature_fahrenheit FROM temperatures;
GROUP BY state ORDER BY state;
