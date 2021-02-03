
import mysql.connector
import models

class Database:
    __instance = None

    def __init__(self,host,user,password,database):
        self.connection = self.connect(host,user,password,database)
        self.cursor = self.connection.cursor()

    @classmethod
    def getInstance(cls,host,user,password,database):
        if Database.__instance is None:
            return Database(host,user,password,database) 
        else:
            return Database.__instance

    def __del__(self):
        self.connection.close()

    def connect(self,host,user,password,database):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
                database=database
            )
            return connection
        except:
            raise RuntimeError('Database not found')

    def exists(self):
        sql = "show count(tables) like 'movies' or 'categories'"
        self.cursor.execute(sql)
        return False if self.cursor.fetchone()[0] == 0 else True

    def migrate(self):
        if not self.exists():
            for table in models.migrations.tables:
                sql = 'create table if not exists %s ( %s );'.format( table['name'] , table['schema'] )
                self.cursor.execute( sql , ( table['name'] , table['schema'] ) )

            category = models.Category(self.url)
            category.setup()
            movie = models.Movie(self.url)
            movie.setup()

            self.connection.commit()

    def formatall(self,rows):
        array = []
        for row in rows:
            data = {}
            names = list(map(lambda x: x[0], self.cursor.description))
            for name in names:
                data[name] = row[name]
            array.append(data)

        return array
    
    def formatone(self,row):
        data = {}
        names = list(map(lambda x: x[0], self.cursor.description))
        for name in names:
            data[name] = row[name]

        return data

