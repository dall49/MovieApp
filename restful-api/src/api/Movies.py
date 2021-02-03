
from models import Movie
from api import Api
from flask import request

class Movies(Api):

    def __init__(self,config):
        super().__init__(config)

    def create_model(self,host,user,password,database):
        self.model = Movie(host,user,password,database)

    def sanitize_data(self):
        data = (
            request.form['title'].lower().capitalize(),
            float( request.form['rating'] ),
            request.form['image'].lower(),
            request.form['category'].lower().capitalize()
        )

        return data
