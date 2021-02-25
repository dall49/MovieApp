
from flask import Flask
from flask_restful import Api 
from flask_cors import CORS
from src.api import Movies , Categories , Upload
from src.models import Database
from os import getcwd

def create_app():
    static_folder = getcwd() + '/img/'
    app = Flask(
        __name__,
        static_folder=static_folder
    )
    CORS(app)
    api = Api(app)

    Database().migrate()

    api.add_resource(Upload,'/upload')
    api.add_resource(Movies,'/movies','/movies/<string:id>')
    api.add_resource(Categories,'/categories','/categories/<string:id>')

    return app

if __name__ == '__main__':
    app = create_app()

    host = '0.0.0.0'
    port = 5000
    debug = True
    
    app.run(host,port,debug)
