from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

app = Flask(__name__)

# Connect to database and create database session
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db_session = DBSession()

# Import modules
import catalog.views
import catalog.models
import catalog.auth
