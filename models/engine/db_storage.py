#!/usr/bin/python3
"""
Building database storage class
"""
from os import getenv
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session

all_classes = {"User": User, "City": City, "State": State, 
"Place": Place, "Review": Review, "Amenity": Amenity}



class DBStorage:
    """
    _engine: the SQLALCHEMY engine
    _session: the SQLALCHEMY session
    """
    __engine = None
    __session = None


    def __init__(self):
        """
        starting up a connection to MySQL a table
        """
        datab = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(datab, pool_pre_ping=True)
        self.reload()
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on current database session
        returns a dictionary
        """
        ent = dict()
        if cls:
            return self.get_data_from_table(cls, ent)
        for entity in all_classes:
            ent = self.get_data_from_table(eval(entity), ent)
        return ent

    def new(self, obj):
        """
        add object to current database session
        """
        if obj:
            self.session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        creates all tables in the database
        creates current database session
        """
        Base.metadata.create_all(self.__engine)
        sesh_creator = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(sesh_creator)
        self.__session = Session()
