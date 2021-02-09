
from src.models import Category
from src.api import Api
from flask import request

class Categories(Api):
    
    def __init__(self):
        super().__init__()

    def create_model(self):
        self.model = Category()
    
    def sanitize_data(self):
        data = [
            request.form['name'].lower().capitalize()
        ]

        return data

