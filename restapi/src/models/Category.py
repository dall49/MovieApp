
from src.models import Database

class Category(Database):
    
    def __init__(self):
        super().__init__()

    def get(self):
        sql = 'select * from categories order by id;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)

    def get_by_id(self,id):
        sql = 'select * from categories where id = %s;'
        try:
            self.cursor.execute(sql,[id,])
            data = self.cursor.fetchone()
            return self.formatone(data)
        except:
            return {}

    def create(self,data):
        sql = 'insert into categories (name) values (%s)'
        self.cursor.execute(sql,data)
        self.connection.commit()
        
        sql = 'select id from categories where name = %s;'
        self.cursor.execute(sql,data)

        return self.cursor.fetchone()['id']
    
    def delete(self):
        sql = 'delete from categories;'
        self.cursor.execute(sql)
        self.connection.commit()

    def delete_by_id(self,id):
        sql = 'delete from movies where category_id = %s;'
        self.cursor.execute(sql,[id,])
        sql = 'delete from categories where id = %s;'
        self.cursor.execute(sql,[id,])
        self.connection.commit()


    def update(self,data):
        name = data[0]
        sql = 'update categories set name = %s where id = %s;'
        try:
            self.cursor.execute(sql,data)
            self.connection.commit()
        except:
            pass


