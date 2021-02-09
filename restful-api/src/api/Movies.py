
from src.models import Movie
from src.api import Api
from flask import request
from os import remove , listdir
from os.path import exists

class Movies(Api):

    def __init__(self):
        super().__init__()
    
    def create_model(self):
        self.model = Movie()

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
            for file in listdir('img/'):
                if valid_file(file):
                    remove('img/'+file)
        else:
            filename = self.model.delete_by_id(id)
            if filename != False:
                if exists('img/'+filename):
                    if valid_file(filename):
                        remove('img/'+filename)

        return {} , 204
