
from flask_restful import Resource
from abc import ABC , abstractmethod

class FinalMeta(type(ABC), type(Resource)):
    pass

class Api(ABC,Resource,metaclass=FinalMeta):

    def __init__(self):
        self.create_model()

    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def sanitize_data(self) -> list:
        pass

    def get(self,id=None):
        data = self.model.get() if id is None else self.model.get_by_id(id)

        return data , 200

    def post(self):
        data = self.sanitize_data()
        id = self.model.create(data)

        return self.model.get_by_id(id) , 201
    
    def delete(self,id=None):
        filename = self.model.delete() if id is None else self.model.delete_by_id(id)

        return {} , 204

    def put(self,id):
        data = self.sanitize_data()
        data.append(id)
        self.model.update(data)

        return self.model.get_by_id(id) , 200
