#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os
import uuid


if os.environ['HBNB_TYPE_STORAGE'] == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now)
        updated_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
            except KeyError:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.id = str(uuid.uuid4())
        self.__dict__.update(kwargs)
        self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = self.to_dict()
        dictionary.pop('__class__')
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        models.storage.delete(self)
