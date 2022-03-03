#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class
    name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", 
                                cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            returns list of City instances with state_id
            equal to the current State.id
            """
            city_l = []
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
