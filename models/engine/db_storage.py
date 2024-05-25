#!/usr/bin/python3
"""DB Storage class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """DB Storage"""
    
    # ... Existing code ...

    def close(self):
        """Method to remove the private session attribute"""
        self.__session.remove()
