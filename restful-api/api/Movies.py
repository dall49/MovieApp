
from models import Movie
from api import Api
from flask import request

class Movies(Api):

    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)
    
    def create_model(self,config):
        self.model = Movie(
            config['host'],
            config['user'],
            config['password'],
            config['database']
        )

    def sanitize_data(self):
        data = [
            request.form['title'].lower().capitalize(),
            float( request.form['rating'] ),
            request.form['image'].lower(),
            request.form['category'].lower().capitalize()
        ]

        return data
