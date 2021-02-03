
from models import Category
from flask_restful import Resource
from flask import request

class Categories(Resource):

    def __init__(self,database_url):
        self.model = Category(database_url)
    
    def get(self,id=None):

        if id is None:
            return self.model.getall()
        else:
            return self.model.getone(id)

    def post(self):
        name = request.form['name']

        return self.model.create(name)
