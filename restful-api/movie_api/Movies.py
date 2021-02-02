
from movie_api import Database

class Movies(Database):

    def __init__(self):
        super().__init__()

    def get(self):
        sql = '''
            select m.id, m.title, m.image, m.rating, c.name
            from movies m inner join categories c
            on m.category_id = c.id;
        '''

        self.cursor.execute(sql.strip())
        data = self.cursor.fetchall()
        fields = ['id','title','image','rating','category']
        data = self.formatall(data,fields)

        return data
        
