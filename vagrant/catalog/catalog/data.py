"""This module includes routes for getting data from the app.

It includes endpoints for getting catalog data in JSON format.
"""

from flask import jsonify

from catalog import app
from catalog import db
from database_setup import User, Category, Item


################################################################################
# JSON
################################################################################

@app.route('/catalog.json')
def view_catalog_json():
    """Catalog in json format."""
    categories = db.query(Category).all()
    items = db.query(Item).all()
    return jsonify(categories = [c.serialize for c in categories],
        items = [i.serialize for i in items])

@app.route("/catalog/category-<int:category_id>.json")
def view_category_json(category_id):
    """Category in json format."""
    category = db.query(Category).filter_by(id = category_id).one()
    items = db.query(Item).filter_by(category_id = category.id).all()
    return jsonify(category = category.serialize,
        items = [i.serialize for i in items])

@app.route("/catalog/item-<int:item_id>.json")
def view_item_json(item_id):
    """Item in json format."""
    item = db.query(Item).filter_by(id = item_id).one()
    return jsonify(item = item.serialize)

@app.route('/users.json')
def users_json():
    """List of users in json format.

    This is for debugging and should probably be removed or protected.

    TODO (pt314): Remove of protect this endpoint.
    """
    users = db.query(User).all()
    return jsonify(users = [u.serialize for u in users])

################################################################################
