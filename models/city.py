#!/usr/bin/python3
""" City Module for HBNB project """
from lib2to3.pytree import Base
import models
from models.base_model import BaseModel
from models.place import Place
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128, nullable=False))
    places = relationship('Place', backref="cities")

    def __init__(self, *args, **kwargs):
        """
        Init for inherited
        """
        super().__init__(*args, **kwargs)
