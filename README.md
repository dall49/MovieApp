# MovieApp

* Description
* Technologies
* Database Schema
* Requirements
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
| image       | varchar(100) | no   |         | default.png |                |
| rating      | float        | no   |         |             |                |
| category_id | int          | no   | foreign |             |                |

## Requirements

All you need to get this project up and running is Docker and Docker Compose.

## Setup

Step 1 : Open a terminal in the root directory : ```MovieApp/```
Step 2 : Run the following command : ```docker-compose up```
