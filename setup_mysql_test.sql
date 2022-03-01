-- Prepairing MySQL for the project
-- database of hbnb_test_db a new user hbnb_test in localhost
-- password of hbnb_test set to hbnb_test_pwd
-- hbnb_test gets all privileges on hbnb_test_db
-- hbnb_test has select privileges on performance_schema
-- if hbnb_test or hbnb_test exists script shouldn't fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS "hbnb_test"@"localhost";
CREATE USER "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO "hbnb_test"@"localhost";
GRANT SELECT ON `performance_schema`.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
