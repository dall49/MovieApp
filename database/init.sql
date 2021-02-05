
create database movieapp;

create user 'movieapp'@'localhost' identified by 'movieapp';

grant all privileges on movieapp.* to 'movieapp'@'localhost';

flush privileges;

use movieapp;

create table if not exists categories ( 
	id int auto_increment,
	name varchar(100) unique not null,
	primary key(id)
);

create table if not exists movies (
	id int auto_increment,
	title varchar(100) unique not null,
	image varchar(100) default 'default.png',
	rating float not null,
	category_id int not null,
	primary key(id),
	foreign key(category_id) references categories(id)
);

