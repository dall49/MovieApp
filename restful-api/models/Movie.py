
import sqlite3
from models import Database

class Movie(Database):

    def __init__(self,url):
        super().__init__(url)

    def setup(self):
        movies = [
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
        ]
        sql = 'insert into movies (title,rating,image,category_id) values (?,?,?,?);'
        self.cursor.executemany(sql, movies)

        self.connection.commit()

    def getall(self):
        sql = '''
            select m.id, m.title, m.image, m.rating, c.name as 'category'
            from movies m inner join categories c
            on m.category_id = c.id;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)

    def getone(self,id):
        sql = '''
            select m.id, m.title, m.image, m.rating, c.name
            from movies m inner join categories c
            on m.category_id = c.id
            where m.id = ?;
        '''
        self.cursor.execute(sql,[id,])
        data = self.cursor.fetchone()
        return self.formatone(data)
    
    def create(self,title,rating,image,category):
        rating = float( rating )

        sql = "select id from categories where name = ?;"
        self.cursor.execute(sql,[category,])
        category_id = int( self.cursor.fetchone()[0] )

        if image != '':
            sql = '''
                insert into movies (title,rating,image,category_id)
                values (?,?,?,?);
            '''
            values = [title,rating,image,category_id]
            self.cursor.execute(sql,values)
        else:
            sql = '''
                insert into movies (title,rating,category_id)
                values (?,?,?);
            '''
            values = [title,rating,category_id]
            self.cursor.execute(sql,values)

        self.connection.commit()

        sql = 'select id from movies where title = ?;'
        self.cursor.execute(sql,[title,])

        return self.cursor.fetchone()[0]


