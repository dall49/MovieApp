
import mysql.connector

class Database:

    def __init__(self,host,user,password,database):
        self.connection = self.connect(host,user,password,database)
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def connect(self,host,user,password,database):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return connection
        except:
            raise RuntimeError('Database not found')

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

