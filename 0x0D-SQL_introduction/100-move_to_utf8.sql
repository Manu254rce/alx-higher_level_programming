-- SCript that converts a SQL table to UTF-8
-- Converting the DB
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert fields
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
