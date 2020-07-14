-- create a database hbtn_0d_usa
-- create a table in hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        FOREIGN KEY(state_id) INT NOT NULL REFERENCES hbtn_0d_usa.states(id),
        name VARCHAR(256) NOT NULL);