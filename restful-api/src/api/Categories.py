
from models import Category
from api import Api
from flask import request

class Categories(Api):
    
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)

    def create_model(self,config):
        self.model = Category(
            config['host'],
            config['user'],
            config['password'],
            config['database']
        )
    
    def sanitize_data(self):
        data = [
            request.form['name'].lower().capitalize()
        ]

        return data

