import httplib2
import requests
import json

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import session as login_session

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

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/logout/")
def logout():
    # for now, just disconnect from google
    return redirect(url_for("google_disconnect"))



################################################################################
# GOOGLE sign-in
################################################################################

from flask import request
from flask import make_response

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import OAuth2Credentials

# Temporary, for debugging.
@app.route('/clearSession')
def clearSession():
    login_session.clear()
    return "Session cleared"

@app.route("/google_connect", methods = ["POST"])
def google_connect():
    # Obtain authorization code
    code = request.data
    print("auth_code: " + code)

    # Upgrade the authorization code into a credentials object.
    try:
        oauth_flow = flow_from_clientsecrets('client_secret_google.json', scope = '')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    print("access_token: " + access_token)
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(
            json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        print "response:", response
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID does not match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['audience'] != app.config.google_client_id:
        response = make_response(
            json.dumps("Token's client ID does not match app's client ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check if user is already connected.
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Everything OK. Now load user info and add things to session...

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    user_info = requests.get(userinfo_url, params = params)

    data = user_info.json()
    print("user_info: " + str(data))

    login_session['provider'] = 'google'
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = '<h1>Welcome, ' + login_session['username'] + '!</h1>'
    output += '<p>' + login_session['email'] + '</p>'
    output += '<img src="' + login_session['picture'] + '" style="width: 200px; height: 200px; border-radius: 100px; -webkit-border-radius: 100px; -moz-border-radius: 100px;">'
    return output


@app.route('/google_disconnect')
def google_disconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('credentials')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print "access_token:", access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print "result:", result

    if result['status'] == '200':
        # Reset the user's session.
        login_session.clear()
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

################################################################################



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
    items = session.query(Item).filter_by(category_id = category.id).all()
    return jsonify(category = category.serialize,
        items = [i.serialize for i in items])



@app.route("/catalog/item/<int:item_id>/")
def view_item(item_id):
    """View a specific item."""
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template("item.html", item = item)

@app.route("/catalog/item/<int:item_id>/json/")
def view_item_json(item_id):
    """Item in json format."""
    item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(item = item.serialize)
