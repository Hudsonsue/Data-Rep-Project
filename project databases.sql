create database datarepresentation;
use datarepresentation;
CREATE TABLE accounts (
  
  username varchar(255) not NULL,
  password varchar(255) NULL,
  PRIMARY KEY (username));
  insert into accounts (username, password) values('suetest', 'spword');
  insert into accounts (username, password) values('admin', 'admin');
  
	SELECT * FROM accounts;
    
CREATE TABLE if not exists orders (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  	Item varchar(100) NOT NULL,
  	About varchar(255) NOT NULL,
  	Quantity int(11) NOT NULL);
select * from orders;

CREATE TABLE if not exists menu (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  	Item varchar(100) NOT NULL,
  	About varchar(25) NOT NULL,
  	Price char(5) NOT NULL);
    
    
select * from orders;
select * from menu;
show tables;