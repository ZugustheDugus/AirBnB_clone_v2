#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

<<<<<<< HEAD
from sqlalchemy import delete

=======
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}
>>>>>>> 6dc681f407fd3252e25eedb4dbdacb80f291ea39

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
<<<<<<< HEAD
            class_objects = {}
            for item in FileStorage.__objects:
                if type(self.__objects[item]) == cls:
                    class_objects[item] = self.__objects[item]
            return class_objects
        else:
            return FileStorage.__objects
=======
            return {key: self.__objects[key] for key in self.__objects if self.__objects[key].__class__ == cls}
        return FileStorage.__objects
>>>>>>> 6dc681f407fd3252e25eedb4dbdacb80f291ea39

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects if the argument matches a valid
        instance.
        """
        if obj == None:
            return
        elif obj in self.__objects.values():
            objk = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(objk, None)

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
