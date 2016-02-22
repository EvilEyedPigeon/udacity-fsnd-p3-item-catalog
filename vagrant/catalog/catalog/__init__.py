import os
import json

from flask import Flask
from flask import render_template

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

app = Flask(__name__)


# Load client ids from config files
app.config['GOOGLE_CLIENT_ID'] = json.loads(open('client_secret_google.json', 'r').read())['web']['client_id']


# Configuration
app_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'super_secret_key'
app.config['CSRF_SECRET_KEY'] = 'csfr_super_secret_key'
app.config['UPLOAD_FOLDER'] = os.path.join(app_dir, '..', 'uploads')
app.config['ALLOWED_IMAGE_EXTENSIONS'] = set(['jpg', 'jpeg', 'png', 'gif'])


# Connect to database and create database session
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db = DBSession()


# Register HTTP error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


# Import modules
import catalog.models

# Register blueprints
from views.api import api
from views.auth import auth
from views.data import data

app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(data)
