
from flask_restful import Resource 
from flask import request
import os
from werkzeug.utils import secure_filename

class Upload(Resource):

    def __init__(self,upload_dir):
        self.upload_dir = upload_dir
        self.allowed_extensions = ['.pdf', '.png', '.jpg', '.jpeg', '.gif']

    def valid_extensions(self,filename):
        extension = os.path.splitext(filename)[1]
        return False if extension not in self.allowed_extensions else True

    def post(self):
        if 'file' not in request.files:
            return {'status':'failed','message':'Data name must be file'} , 400

        file = request.files['file']
        filename = file.filename

        if filename == '':
            return {'status':'failed','message':'Empty filename'} , 400
        elif not self.valid_extensions(filename):
            return {'status':'failed','message':'Wrong file extension'} , 400

        if not os.path.isdir(self.upload_dir):
            os.mkdir(self.upload_dir)

        filename = secure_filename(filename)
        file.save( os.path.join(self.upload_dir,filename) )

        return {'status':'success','filename':filename } , 201
