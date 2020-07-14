-- create a database hbtn_0d_usa
-- create a table in hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL;
       FOREIGN KEY(state_id) NOT NULL REFERENCES hbtn_0d_usa.states(id))
       