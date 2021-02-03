
from flask import Flask 
from flask_restful import Api 
from flask_cors import CORS
from api import Movies , Categories
from models import Database

app = Flask(__name__)
CORS(app)
api = Api(app)
database_url = 'movie.db'

database = Database(database_url)
database.migrate()

kwargs = { 'database_url' : database_url }

api.add_resource( Movies,'/movies','/movies/<string:id>',resource_class_kwargs=kwargs )
api.add_resource( Categories,'/categories','/categories/<string:id>',resource_class_kwargs=kwargs )

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    debug = True
    app.run(host,port,debug)
