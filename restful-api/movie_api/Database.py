
from movie_api import Resource , sqlite3

class Database(Resource):

    def __init__(self):
        self.connection = sqlite3.connect('movie.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def formatall(self,rows,fields):
        array = []
        for row in rows:
            data = {}
            names = list(map(lambda x: x[0], self.cursor.description))
            for field , name in zip(fields,names):
                data[field] = row[name]
            array.append(data)

        return array
    
    def format(self,row,fields):
        data = {}
        names = list(map(lambda x: x[0], self.cursor.description))
        for field , name in zip(fields,names):
            data[field] = row[name]

        return data

    def setup(self):
        sql = '''
            create table categories (
                id integer primary key autoincrement,
                name varchar(100)
            );
        '''
        self.cursor.execute(sql.strip())

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
        
        sql = '''
            create table if not exists movies (
                id integer primary key autoincrement,
                title varchar(100),
                image varchar(100),
                rating float,
                category_id integer,
                foreign key (category_id) references categories(id)
            );
        '''
        self.cursor.execute(sql.strip())

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

