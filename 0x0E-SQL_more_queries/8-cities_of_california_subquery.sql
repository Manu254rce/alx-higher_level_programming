-- Script that lists all citis of a state(Cafornia) that are inside the databbase
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = (
	SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
