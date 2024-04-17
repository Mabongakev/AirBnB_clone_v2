#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import Base, BaseModel
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State"""
        super().__init__(*args, **kwargs)


# State.cities = relationship("City", order_by=City.id, back_populates='state')
