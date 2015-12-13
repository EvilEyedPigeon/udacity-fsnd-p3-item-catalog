from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


##### classes/tables #####

class User(Base):
    """Application user.

    Attributes:
        id (Integer): 
            User ID.
        name (String): 
            User name.
            Usually this includes the user's given name and last name.
        email (String):
            User email.
        picture (String):
            Picture URL.
            The picture may be stored on an external server, for example,
            when using third party authentication.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(256), nullable = False)
    email = Column(String(256), nullable = False)
    picture = Column(String)

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
    """Item category.

    Attributes:
        id (Integer): 
            Category ID.
        name (String): 
            Category name.
    """
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
    """Individual item.

    Attributes:
        id (Integer): 
            Item ID.
        name (String): 
            Item name.
        description (String):
            Item description.
        image (String):
            Image file name.
            The actual image is stored on the file system.
        category_id (Integer):
            ID of this item's category.
        category (Category):
            This item's category.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)
    description = Column(String)
    image = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id'            : self.id,
            'name'          : self.name,
            'description'   : self.description,
            'image'         : self.image,
            'category_id'   : self.category_id
        }


##### create database #####

engine = create_engine('sqlite:///item_catalog.db')

Base.metadata.create_all(engine)
