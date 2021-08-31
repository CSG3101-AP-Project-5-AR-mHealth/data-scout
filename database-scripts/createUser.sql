-- Create user with permisisons to vitals db
CREATE USER 'test'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON vitalsdb.* TO 'test'@'localhost';
FLUSH PRIVILEGES;
