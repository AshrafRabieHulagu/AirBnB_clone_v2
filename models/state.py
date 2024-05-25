#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """State class"""

    # ... Existing code ...

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter method to return the list of City objects linked to the current State"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
