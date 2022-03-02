#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.city import City


class State(BaseModel):
    """ State class
    name: input name
    """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            """
            returns list of City insatnces with state_id
            equal to the current State.id
            """
            cities = list()
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
