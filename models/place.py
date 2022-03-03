#!/usr/bin/python3
""" Place Module for HBNB project """
from tokenize import String
from AirBnB_clone_v2.models.base_model import Base
from models.base_model import BaseModel
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv
from models.amenity import Amenity
from models.review import Review


place_amenity = Table("place_amenity", Base.metadata, Column
                        ("place_id", String(60), ForeignKey
                        ("places.id"), primary_key=True,
                        nullable=False), Column("amenity_id",
                        String(60), ForeignKey("amenities.id"),
                        primary_key=True, nullable=False))
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    __tablename__ = "place_amenity"
    place_amenities = relationship('Place', secondary=place_amenity)
    metadata = Base.metadata

