from flask import Flask
from flask import render_template
from flask import url_for
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item

import json

app = Flask(__name__)


# Connect to database and create database session

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


# Temporary, for testing
catalog = ["Phone", "Book", "Blue pen", "Banana"]


@app.route("/hello/")
def hello():
    output = "<html>"
    output += "<body>"
    output += "<p>Hello World!</p>"
    output += "<p>Welcome to the item catalog web app :)</p>"
    output += "<p><a href = " + url_for("view_catalog") + ">View catalog</a></p>"
    output += "</body>"
    output += "</html>"
    return output

@app.route("/")
@app.route("/catalog/")
def view_catalog():
    categories = session.query(Category).all()
    items = session.query(Item).all()
    return render_template("catalog.html", categories = categories, items = catalog)

@app.route('/catalog.json')
def view_catalog_json():
    return json.dumps(catalog)


# Start the app
if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
 