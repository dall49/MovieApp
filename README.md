# MovieApp

* Description
* Technologies
* Database Schema
* Setup

## Description

MovieApp is a small CRUD app that allows you to create a movie and see your saved movies.

## Technologies 

* Front End
	* React 
* Back End 
	* Flask RESTful
* Database
	* MariaDB / MySQL

## Database Schema

### Categories Table

| Field | Type         | Null | KEY     | Default | Extra          |
|-------|--------------|------|---------|---------|----------------|
| id    | int          | no   | primary |         | auto_increment |
| name  | varchar(100) | no   |         |         | unique         |

### Movies Table

| Field       | Type         | Null | KEY     | Default     | Extra          |
|-------------|--------------|------|---------|-------------|----------------|
| id          | int          | no   | primary |             | auto_increment |
| title       | varchar(100) | no   |         |             | unique         |
| image       | varchar(100) | no   |         | default.jpg |                |
| rating      | float        | no   |         |             |                |
| category_id | int          | no   | foreign |             |                |

## Setup

## Back End Setup

### Python

Install python 3.x and pip on your system and follow these steps

* Step 1 : Make sure you are on the right directory ```restful-api/```
* Step 2 : Install globally the awesome tool : pipenv ```pip install pipenv```
* Step 3 : Setup your project : ```pipenv install```
* Step 4 : Activate the virtual environement : ```pipenv shell```
* Step 5 : Run the dev server : ```python app.py```

### MySQL

Install MySQL or MariaDB Server on your system and follow these steps

* Step 1 : Make sure you are on the right directory ```database/```
* Step 2 : Run this command with a super user such as root : ```mysql -u root -p < init.sql```
* Step 3 ( Optional ) : To reset the database run this command : ```mysql -u root -p < destroy.sql```
followed by Step 2

## Front End Setup

Make sure you have the lastest version of npm and nodejs installed on your system

* Step 1 : Make sure you are on the right directory ```web-app/```
* Step 2 : Run the dev server with : ```npm start```

