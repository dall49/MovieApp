
from movie_api import Database

class Categories(Database):

    def __init__(self):
        super().__init__()
    
    def get(self,id=None):
        if id is None:
            sql = 'select * from categories;'
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            fields = ['id','category']
            data = self.formatall(data,fields)
        else:
            sql = 'select * from categories where id = ?;'
            self.cursor.execute(sql,id)
            data = self.cursor.fetchone()
            fields = ['id','category']
            data = self.format(data,fields)

        return data

