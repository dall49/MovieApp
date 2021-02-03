
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
	* Sqlite

## Database Schema

### Categories Table

| Field | Type         | Null | KEY     | Default | Extra         |
|-------|--------------|------|---------|---------|---------------|
| id    | integer      | no   | primary |         | autoincrement |
| name  | varchar(100) | no   |         |         | unique        |

### Movies Table

| Field       | Type         | Null | KEY     | Default     | Extra         |
|-------------|--------------|------|---------|-------------|---------------|
| id          | integer      | no   | primary |             | autoincrement |
| title       | varchar(100) | no   |         |             | unique        |
| image       | varchar(100) | no   |         | default.jpg |               |
| rating      | float        | no   |         |             |               |
| category_id | integer      | no   | foreign |             |               |

## Setup

## Back End Setup

N.B : Make sur you have python 3.x and pip installed on your system

* Step 1 : Make sur you are on the right directory ```restful-api/```
* Step 2 : Install globally the awesome tool : pipenv ```pip install pipenv```
* Step 3 : Setup your project : ```pipenv install```
* Step 4 : Activate the virtual environement : ```pipenv shell```
* Step 5 : Run the dev server : ```python app.py```

## Front End Setup

N.B : Make sure you have the lastest version of npm and nodejs installed on your system

* Step 1 : Make sure you are on the right directory ```web-app/```
* Step 2 : open your terminal
* Step 3 : Run your server with : ```npm start```