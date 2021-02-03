
import sqlite3
from models import Database

class Category(Database):
    
    def __init__(self,url):
        super().__init__(url)

    def setup(self):
        categories = [
            (1,'Romantic'),
            (2,'Action'),
            (3,'Adventure'),
            (4,'Thriller'),
            (5,'Drama')
        ]
        
        sql = 'insert into categories (id,name) values (?,?);'
        self.cursor.executemany(sql, categories)

        self.connection.commit()

    def getall(self):
        sql = 'select * from categories;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)

    def getone(self,id):
        try:
            sql = 'select * from categories where id = ?;'
            self.cursor.execute(sql,[id,])
            data = self.cursor.fetchone()
            return self.formatone(data)
        except:
            return { 'status' : 'failed' }

    def create(self,name):
        try:
            sql = 'insert into categories (name) values (?)'
            self.cursor.execute(sql,[name,])
            self.connection.commit()

            return { 'status' : 'success' }
        except:
            return { 'status' : 'failed' }
