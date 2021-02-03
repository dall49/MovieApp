
from models import Movie
from flask_restful import Resource
from flask import request

class Movies(Resource):

    def __init__(self,database_url):
        self.model = Movie(database_url)

    def get(self,id=None):

        if id is None:
            return self.model.getall()
        else:
            return self.model.getone(id)

    def post(self):
        title = request.form['title']
        rating = request.form['rating']
        image = request.form['image']
        category = request.form['category']

        id = self.model.create(title,rating,image,category)

        return self.model.getone(id)
