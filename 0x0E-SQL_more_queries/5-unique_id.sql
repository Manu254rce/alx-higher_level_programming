-- Scrit that creates a new table with a unique id
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1 NOT NULL,
	name VARCHAR(256)
);
