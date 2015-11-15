from flask import Flask
from flask import render_template

import json

app = Flask(__name__)

# Temporary, for testing
catalog = ["Phone", "Book", "Blue pen", "Banana"]


@app.route("/hello/")
def hello():
    return "Hello World!"

@app.route("/")
@app.route("/catalog/")
def show_catalog():
	return render_template("catalog.html", items = catalog)

@app.route('/catalog.json')
def show_catalog_json():
    return json.dumps(catalog)


if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
 