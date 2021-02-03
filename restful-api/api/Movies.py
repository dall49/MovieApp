
from models import Movie
from api import Api
from flask import request

class Movies(Api):

    def __init__(self,database_url):
        super().__init__(database_url)

    def create_model(self):
        self.model = Movie(self.database_url)

    def sanitize_data(self):
        data = (
            request.form['title'].lower().capitalize(),
            float( request.form['rating'] ),
            request.form['image'].lower(),
            request.form['category'].lower().capitalize()
        )

        return data
