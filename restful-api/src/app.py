
from flask import Flask
from flask_restful import Api 
from flask_cors import CORS

from api import Movies , Categories , Upload

import config

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(
    Upload, 
    '/upload', 
    resource_class_kwargs=config.upload
)

api.add_resource( 
    Movies,
    '/movies','/movies/<string:id>',
    resource_class_kwargs=config.database
)

api.add_resource( 
    Categories,
    '/categories','/categories/<string:id>',
    resource_class_kwargs=config.database
)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    debug = True
    app.run(host,port,debug)
