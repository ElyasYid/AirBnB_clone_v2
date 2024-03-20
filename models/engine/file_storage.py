#!/usr/bin/python3
"""defines class to manage file storage for hbnb clone"""
import json
import os
from importlib import import_module


class FileStorage:
    """class for  storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """Returns a dict of models in storage"""
        if cls is None:
            return self.__objects
        else:
            c_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    c_dict[key] = value
            return c_dict

    def delete(self, obj=None):
        """Removes obj from storage dictionary"""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new obj storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as file:
            kamp = {}
            for key, val in self.__objects.items():
                kamp[key] = val.to_dict()
            json.dump(kamp, file)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            iola = {}
            with open(self.__file_path, 'r') as file:
                iola = json.load(file)
                for key, val in iola.items():
                    self.all()[key] = classes[val['__class__']](**val)

    def close(self):
        """Closes the storage engine."""
        self.reload()
