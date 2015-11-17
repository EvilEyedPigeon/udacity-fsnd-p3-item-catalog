from flask import Flask
from flask import render_template
from flask import url_for
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item

app = Flask(__name__)


# Connect to database and create database session

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



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
    """Catalog homepage."""
    categories = session.query(Category).all()
    items = session.query(Item).all()
    return render_template("catalog.html", categories = categories, items = items)

@app.route('/catalog/json/')
def view_catalog_json():
    """Catalog in json format."""
    categories = session.query(Category).all()
    items = session.query(Item).all()
    return jsonify(categories = [c.serialize for c in categories],
        items = [i.serialize for i in items])



@app.route("/catalog/category/<int:category_id>/")
def view_category(category_id):
    """View a specific category."""
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category.id)
    return render_template("category.html", category = category, items = items)

@app.route("/catalog/category/<int:category_id>/json/")
def view_category_json(category_id):
    """Category in json format."""
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category.id)
    return jsonify(category = category.serialize,
        items = [i.serialize for i in items])



# Start the app
if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
 