from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


##### classes/tables #####

class User(Base):
    """Application user."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(256), nullable = False)
    email = Column(String(256), nullable = False)
    picture = Column(String)    # picture url

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id'           : self.id,
            'name'         : self.name,
            'email'        : self.email,
            'picture'      : self.picture
        }


class Category(Base):
    """Item category."""

    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id'            : self.id,
            'name'          : self.name
        }


class Item(Base):
    """Individual item."""

    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id'            : self.id,
            'name'          : self.name,
            'category_id'   : self.category_id
        }


##### create database #####

engine = create_engine('sqlite:///item_catalog.db')

Base.metadata.create_all(engine)
