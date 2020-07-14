-- create a database hbtn_0d_usa
-- create a table cities in hbtn_0d_usa that inherits a foreign key id from states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id NOT NULL,
       name VARCHAR(256) NOT NULL,
       state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa.states(id) )
       