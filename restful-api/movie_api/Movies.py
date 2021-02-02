
from movie_api import Database

class Movies(Database):

    def __init__(self):
        super().__init__()

    def get(self,id=None):
        if id is None:
            sql = '''
                select m.id, m.title, m.image, m.rating, c.name
                from movies m inner join categories c
                on m.category_id = c.id;
            '''

            self.cursor.execute(sql.strip())
            data = self.cursor.fetchall()
            fields = ['id','title','image','rating','category']
            data = self.formatall(data,fields)
        else:
            sql = '''
                select m.id, m.title, m.image, m.rating, c.name
                from movies m inner join categories c
                on m.category_id = c.id
                where m.id = ?;
            '''

            self.cursor.execute(sql.strip(),id)
            data = self.cursor.fetchone()
            fields = ['id','title','image','rating','category']
            data = self.format(data,fields)

        return data
        
