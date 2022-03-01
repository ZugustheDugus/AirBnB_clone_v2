-- prepairing MySQL for the project using database hbnb_dev_db
-- a new user in localhost
-- password is password jk its hbnb_dev_pwd
-- hbnb_dev has all privileges on the db
-- hbnb_dev has select privileges on performance_schema
-- if hbnb_dev_db or user hbnb_dev already exists script should'nt fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS "hbnb_dev"@"localhost";
CREATE USER "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON `performance_schema`.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
