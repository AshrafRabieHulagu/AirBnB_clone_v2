#!/usr/bin/python3
"""File Storage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes to instances"""
    
    # ... Existing code ...

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
