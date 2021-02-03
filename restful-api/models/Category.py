
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

    def get(self):
        sql = 'select * from categories;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)

    def get_by_id(self,id):
        sql = 'select * from categories where id = ?;'
        self.cursor.execute(sql,[id,])
        data = self.cursor.fetchone()
        return self.formatone(data)

    def create(self,data):
        name = data

        sql = 'insert into categories (name) values (?)'
        self.cursor.execute(sql,[name,])
        self.connection.commit()
        
        sql = 'select id from categories where name = ?;'
        self.cursor.execute(sql,[name,])

        return self.cursor.fetchone()[0]
    
    def delete(self):
        sql = 'delete from movies;'
        self.cursor.execute(sql)
        sql = 'delete from categories;'
        self.cursor.execute(sql)
        self.connection.commit()

    def delete_by_id(self,id):
        sql = 'delete from movies where category_id = ?;'
        self.cursor.execute(sql,[id,])
        sql = 'delete from categories where id = ?;'
        self.cursor.execute(sql,[id,])
        self.connection.commit()


    def update(self,id,data):
        name = data
        sql = 'update categories set name = ? where id = ?;'
        data = [name,id]
        self.cursor.execute(sql,data)
        self.connection.commit()


