
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
	image varchar(100) default 'default.jpg',
	rating float not null,
	category_id int not null,
	primary key(id),
	foreign key(category_id) references categories(id)
);

insert into categories (id,name)
values
	(1,'Romantic'),
	(2,'Action'),
	(3,'Adventure'),
	(4,'Thriller'),
	(5,'Drama');

insert into movies (title,rating,image,category_id)
values
	('Casablanca',8.5,'casablanca.jpg',1),
	('King Kong',7.2,'king_kong.jpg',2),
	('Marriage Story',7.9,'marriage_story.jpg',1),
	('Interstellar',8.6,'interstellar.jpg',3),
	('Avengers Endgame',8.4,'avengers.jpg',2),
	('Get Out',7.7,'get_out.jpg',4),
	('Titanic',7.8,'titanic.jpg',5),
	('Indiana Jones',8.4,'indiana_jones.jpg',3),
	('Godzilla',6.4,'godzilla.jpg',2),
	('Jurassic Park',8.1,'jurassic_park.jpg',2)
