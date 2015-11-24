import httplib2
import requests
import json

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import jsonify
from flask import session as login_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

app = Flask(__name__)

# Connect to database and create database session
engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
db_session = DBSession()

import catalog.models
import catalog.auth



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

# @app.route("/login/")
# def login():
#     return render_template("login.html")

# @app.route("/logout/")
# def logout():
#     # for now, just disconnect from google
#     return redirect(url_for("google_disconnect"))


################################################################################
# View catalog
################################################################################

@app.route("/")
@app.route("/catalog/")
def view_catalog():
    """Catalog homepage."""
    categories = db_session.query(Category).all()
    items = db_session.query(Item).all()
    return render_template("catalog.html", categories = categories, items = items)

@app.route('/catalog/json/')
def view_catalog_json():
    """Catalog in json format."""
    categories = db_session.query(Category).all()
    items = db_session.query(Item).all()
    return jsonify(categories = [c.serialize for c in categories],
        items = [i.serialize for i in items])



@app.route("/catalog/category/<int:category_id>/")
def view_category(category_id):
    """View a specific category."""
    category = db_session.query(Category).filter_by(id = category_id).one()
    items = db_session.query(Item).filter_by(category_id = category.id)
    return render_template("category.html", category = category, items = items)

@app.route("/catalog/category/<int:category_id>/json/")
def view_category_json(category_id):
    """Category in json format."""
    category = db_session.query(Category).filter_by(id = category_id).one()
    items = db_session.query(Item).filter_by(category_id = category.id).all()
    return jsonify(category = category.serialize,
        items = [i.serialize for i in items])



@app.route("/catalog/item/<int:item_id>/")
def view_item(item_id):
    """View a specific item."""
    item = db_session.query(Item).filter_by(id = item_id).one()
    return render_template("item.html", item = item)

@app.route("/catalog/item/<int:item_id>/json/")
def view_item_json(item_id):
    """Item in json format."""
    item = db_session.query(Item).filter_by(id = item_id).one()
    return jsonify(item = item.serialize)


################################################################################
# Create/edit items
################################################################################

@app.route("/catalog/item/new/", methods = ['GET', 'POST'])
def new_item():
    """Create new item."""
    if request.method != 'POST':
        categories = db_session.query(Category).order_by(Category.name).all() # sort alphabetically
        return render_template('new_item.html', categories = categories)
    new_item = Item(
        name = request.form['name'],
        description = request.form['description'],
        category_id = request.form['category_id'])
    db_session.add(new_item)
    db_session.commit()
    return redirect(url_for('view_catalog'))


################################################################################
