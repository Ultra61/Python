\connect root@localhost
CREATE DATABASE whatabook;
USE whatabook;
CREATE TABLE book (book_id
CREATE TABLE `whatabook`.`book` (
  `book_id` INT NOT NULL AUTO_INCREMENT,
  `book_name` VARCHAR(200) NOT NULL,
  `details` VARCHAR(500) NULL DEFAULT NULL,
  `author` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`book_id`));
 CREATE TABLE `whatabook`.`store` (
  `store_id` INT NOT NULL,
  `locale` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`store_id`));
CREATE TABLE `whatabook`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(75) NOT NULL,
  `last_name` VARCHAR(75) NOT NULL,
  PRIMARY KEY (`user_id`));
CREATE TABLE `whatabook`.`wishlist` (
  `wishlist_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`wishlist_id`));
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('1', 'Wizards Tale', 'Fantasy Fiction', 'Sherri Barnes');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('2', 'Avian Creatures', 'Nonfiction', 'Jeff Kale');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('3', 'Space Adventure', 'Science Fiction', 'Carole High');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('4', 'Body by the River', 'Mystery', 'Cassidy Red');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('5', 'The Past Revealed', 'Historical Fiction', 'Allen Halberd');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('6', 'Ancient Egypt', 'History', 'Marcus Terry');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('7', 'The Greatest Love Story', 'Romance', 'Isabella Berry');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('8', 'Penguins Uncut', 'Fiction', 'Randalf Brahman');
INSERT INTO `whatabook`.`book` (`book_id`, `book_name`, `details`, `author`) VALUES ('9', 'President', 'Biography', 'Harry McDuffie');
INSERT INTO `whatabook`.`store` (`store_id`, `locale`) VALUES ('1', '2342 Ashberry Avenue, Yeetown Ohio, 47525');
INSERT INTO `whatabook`.`user` (`user_id`, `first_name`, `last_name`) VALUES ('1', 'Jake ', 'Limbo');
INSERT INTO `whatabook`.`user` (`user_id`, `first_name`, `last_name`) VALUES ('2', 'Brittini', 'Jacobs');
INSERT INTO `whatabook`.`user` (`user_id`, `first_name`, `last_name`) VALUES ('3', 'Rosie', 'Greenwood');
INSERT INTO `whatabook`.`wishlist` (`wishlist_id`, `user_id`, `book_id`) VALUES ('1', '1', '7');
INSERT INTO `whatabook`.`wishlist` (`wishlist_id`, `user_id`, `book_id`) VALUES ('2', '2', '4');
INSERT INTO `whatabook`.`wishlist` (`wishlist_id`, `user_id`, `book_id`) VALUES ('3', '3', '2');