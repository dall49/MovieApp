
from models import Movie
from flask_restful import Resource

class Movies(Resource):

    def __init__(self,database_url):
        self.model = Movie(database_url)

    def get(self,id=None):

        if id is None:
            return self.model.getall()
        else:
            return self.model.getone(id)
