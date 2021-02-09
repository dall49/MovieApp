
import mysql.connector as mysql
from config import database as config

class Database:

    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def migrate(self):
        sql = '''
        create table if not exists categories ( 
            id int auto_increment,
            name varchar(100) unique not null,
            primary key(id)
        );
        '''
        self.cursor.execute(sql)
        sql = '''
        create table if not exists movies (
            id int auto_increment,
            title varchar(100) unique not null,
            image varchar(100) default 'default.png',
            rating float not null,
            category_id int not null,
            primary key(id),
            foreign key(category_id) references categories(id) on delete cascade
        );
        '''
        self.cursor.execute(sql)

    def connect(self):
        connection = mysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            database=config['DATABASE'],
            port=config['PORT']
        )
        return connection

    def formatall(self,rows):
        array = []
        for row in rows:
            data = {}
            names = list(map(lambda x: x[0], self.cursor.description))
            for name in names:
                data[name] = row[name]
            array.append(data)

        return array
    
    def formatone(self,row):
        data = {}
        names = list(map(lambda x: x[0], self.cursor.description))
        for name in names:
            data[name] = row[name]

        return data

