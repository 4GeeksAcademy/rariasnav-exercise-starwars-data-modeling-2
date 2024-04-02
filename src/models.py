import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
    
class Starship(Base):
    __tablename__='starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model= Column(String(250))
    cargo_capacity = Column(Integer)

    def to_dict(self):
        return{}

class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    diameter = Column(Integer)

    def to_dict(self):
        return{}

class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    homeworld = Column(Integer, ForeignKey('planet.id'))
    vehicles = Column(Integer, ForeignKey('starship.id'))
    starship = relationship(Starship)
    planet = relationship(Planet)

    def to_dict(self):
        return{}
    





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
