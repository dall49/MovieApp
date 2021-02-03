
from models import Category
from api import Api
from flask import request

class Categories(Api):

    def __init__(self,config):
        super().__init__(config)

    def create_model(self,host,user,password,database):
        self.model = Category(host,user,password,database)
    
    def sanitize_data(self):
        data = ( 
            request.form['name'].lower().capitalize()
        )

        return data

