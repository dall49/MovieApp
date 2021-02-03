
from models import Category
from api import Api
from flask import request

class Categories(Api):

    def __init__(self,database_url):
        super().__init__(database_url)

    def create_model(self):
        self.model = Category(self.database_url)
    
    def sanitize_data(self):
        data = ( 
            request.form['name'].lower().capitalize()
        )

        return data

