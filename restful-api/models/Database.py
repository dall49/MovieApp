
import sqlite3
import os
import migrations
import models

class Database:

    def __init__(self,url):
        self.url = url
        self.connect()

    def __del__(self):
        self.connection.close()

    def connect(self):
        self.connection = sqlite3.connect(self.url)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def exists(self):
        sql = "select count(name) from sqlite_master where name='movies' or name='categories'"
        self.cursor.execute(sql)
        if self.cursor.fetchone()[0] == 0:
            return False
        return True 

    def migrate(self):
        if not self.exists():
            for table in migrations.tables:
                sql = 'create table if not exists {} ( {} );'.format( table['name'] , table['schema'] )
                self.cursor.execute(sql)

            category = models.Category(self.url)
            category.setup()
            movie = models.Movie(self.url)
            movie.setup()

            self.connection.commit()

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

