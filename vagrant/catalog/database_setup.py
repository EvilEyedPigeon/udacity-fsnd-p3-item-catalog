from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


##### classes/tables #####

class Category(Base):
    """Item category."""

    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)

    name = Column(String(120), nullable = False)


class Item(Base):
    """Individual item."""

    __tablename__ = "items"

    id = Column(Integer, primary_key = True)

    name = Column(String(120), nullable = False)

    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship(Category)


##### create database #####

engine = create_engine('sqlite:///item_catalog.db')

Base.metadata.create_all(engine)
