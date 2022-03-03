#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table("place_amenity", Base.metadata, Column
                        ("place_id", String(60), ForeignKey
                        ("places.id"), primary_key=True,
                        nullable=False), Column("amenity_id",
                        String(60), ForeignKey("amenities.id"),
                        primary_key=True, nullable=False))
class Amenity(BaseModel, Base):
    """
    name: Amenities name
    Place_amenities(relationship): Place = Amenitity relationship
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""

    """def __init__(self, *args, **kwargs):
        "
        Init for inherited
        "
        super().__init__(*args, **kwargs)"""
