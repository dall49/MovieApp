

from src.models import Database

class Movie(Database):

    def __init__(self):
        super().__init__()

    def get(self):
        sql = '''
            select m.id, m.title, m.image, m.rating, c.name as 'category'
            from movies m inner join categories c
            on m.category_id = c.id
            order by id;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return self.formatall(data)

    def get_by_id(self,id):
        sql = '''
            select m.id, m.title, m.image, m.rating, c.name
            from movies m inner join categories c
            on m.category_id = c.id
            where m.id = %s;
        '''
        try:
            self.cursor.execute(sql,[id,])
            data = self.cursor.fetchone()
            return self.formatone(data)
        except:
            return {}

    def get_category_id(self,name):
        sql = "select id from categories where name = %s;"
        self.cursor.execute(sql,[name,])
        fetched = self.cursor.fetchone()
        return False if fetched is None else fetched['id']
       
    def create_category(self,name):
        sql = 'insert into categories (name) values (%s);'
        self.cursor.execute(sql,[name,])
        self.connection.commit()

    def create(self,data):
        category = data[3]
        title = data[0]

        category_id = self.get_category_id(category)
        if category_id == False:
            self.create_category(category)
            category_id = self.get_category_id(category)

        data[3] = category_id
        if data[2] == '':
            data.pop(2)
            sql = 'insert into movies (title,rating,category_id) values (%s,%s,%s);'
        else:
            sql = 'insert into movies (title,rating,image,category_id) values (%s,%s,%s,%s);'

        self.cursor.execute(sql,data)
        self.connection.commit()

        sql = 'select id from movies where title = %s;'
        self.cursor.execute(sql,[title,])

        return self.cursor.fetchone()['id']

    def delete(self):
        sql = 'delete from movies;'
        self.cursor.execute(sql)
        self.connection.commit()

    def delete_by_id(self,id):
        sql = 'select image from movies where id = %s;'
        self.cursor.execute(sql,[id,])
        fetched = self.cursor.fetchone()
        if fetched is not None:
            filename = fetched['image']
            sql = 'delete from movies where id = %s;'
            self.cursor.execute(sql,[id,])
            self.connection.commit()
            return filename
        return False

    def update(self,data):
        title = data[0]
        category = data[3]

        category_id = self.get_category_id(category)
        if category_id == False:
            self.create_category(category)
            category_id = self.get_category_id(category)
        
        data[3] = category_id 

        sql = 'update movies set title = %s , rating = %s , image = %s , category_id = %s where id = %s;'
        try:
            self.cursor.execute(sql,data)
            self.connection.commit()
        except:
            pass


