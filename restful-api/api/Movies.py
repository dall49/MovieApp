
from models import Movie
from api import Api
from flask import request
import os

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
    
    def delete(self,id=None):
        valid_file = lambda f : f != 'default.png'
        if id is None:
            self.model.delete()
            for file in os.listdir('img/'):
                if valid_file(file):
                    os.remove('img/'+file)
        else:
            filename = self.model.delete_by_id(id)
            if valid_file(filename):
                os.remove('img/'+filename)

        return {} , 204
