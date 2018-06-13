#!/usr/bin/python3
""" defines all common attributes/methods for other classes """
import uuid
import datetime
import json
from models import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Initialise class BaseMode
        Args:
            *args - not used
            **kwargs - dictionary, contains arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.datetime.strptime
                        (value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """updates the public attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['id'] = self.id
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict

    def __str__(self):
        """returns string with the BaseModel arguments"""
        return "[%s] (%s) %s" % \
            (self.__class__.__name__, self.id, self.__dict__)
