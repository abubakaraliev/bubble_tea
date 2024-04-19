CREATE DATABASE IF NOT EXISTS bubble_db;

USE bubble_db;

CREATE TABLE IF NOT EXISTS `Products`(
    id INT AUTO_INCREMENT PRIMARY KEY,
    identifier VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    is_available BOOL NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS `Users`(
    `username` VARCHAR(255) NOT NULL PRIMARY KEY,
    `password` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Users_informations`(
    `lastname` VARCHAR(255) NOT NULL PRIMARY KEY,
    `firstname` VARCHAR(255) NOT NULL,
    `phone` INTEGER NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `postcode` INTEGER NOT NULL,
    `city` VARCHAR(255) NOT NULL,
);

CREATE TABLE IF NOT EXISTS `Orders`(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255) NOT NULL,
    product_id INT NOT NULL,
    sugar INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (user) REFERENCES Users(username),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);
CREATE TABLE IF NOT EXISTS `UserInformation` (
    `username` VARCHAR(255) NOT NULL,
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `address` VARCHAR(255) NOT NULL,
    `phone_number` VARCHAR(255),
    PRIMARY KEY (`username`),
    FOREIGN KEY (`username`) REFERENCES `Users`(`username`) ON DELETE CASCADE
);
