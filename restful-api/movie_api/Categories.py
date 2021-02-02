
from movie_api import Database

class Categories(Database):

    def __init__(self):
        super().__init__()
    
    def get(self):
        sql = 'select * from categories;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        fields = ['id','category']
        data = self.formatall(data,fields)

        return data

