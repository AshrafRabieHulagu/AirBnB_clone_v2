#!/usr/bin/python3
"""Defines filestorage class"""
import json


class FileStorage:
    """
    Represents abtracted storage engine

    Attributes:
        __objects (dict): dictionary of instantiated obj
        __file_path (str): name of file to save objects to
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns list: list of __object"""
        my_dict = {}
        if cls:
            for key, value in self.__objects.items():
                if key.startswith(str(cls.__name__)):
                    my_dict[key] = value
        else:
            my_dict = self.__objects
        return my_dict

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
