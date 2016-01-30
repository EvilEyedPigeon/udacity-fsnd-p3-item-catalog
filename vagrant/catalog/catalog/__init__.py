import os

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

app = Flask(__name__)

# Configuration
app_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(app_dir, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect to database and create database session
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db = DBSession()

# Import modules
import catalog.models

# Register blueprints
from views.api import api
from views.auth import auth
from views.data import data

app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(data)
