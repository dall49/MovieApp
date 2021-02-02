
from flask import Flask 
from flask_restful import Api 
from movie_api import Database , Movies , Categories
import os

app = Flask(__name__)
api = Api(app)

if not os.path.exists('movie.db'):
    print('Setting up...')
    Database().setup()

api.add_resource(Movies , '/movies')
api.add_resource(Categories , '/categories')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    debug = True
    app.run(host,port,debug)
