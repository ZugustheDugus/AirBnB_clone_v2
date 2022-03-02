#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD

from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
=======
from lib2to3.pytree import Base
import models
>>>>>>> da02fd71e771b64b5074f5179dfcc50e823c2d64
from models.base_model import BaseModel
from models.place import Place
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")

    else:
        state_id = ""
        name = ""
=======
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128, nullable=False))
    places = relationship('Place', backref="cities")

    def __init__(self, *args, **kwargs):
        """
        Init for inherited
        """
        super().__init__(*args, **kwargs)
>>>>>>> da02fd71e771b64b5074f5179dfcc50e823c2d64
