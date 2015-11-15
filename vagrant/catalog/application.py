from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hello/")
def hello():
    return "Hello World!"

@app.route("/")
@app.route("/catalog/")
def show_catalog():
	items = ["Phone", "Book", "Blue pen", "Banana"]
	return render_template("catalog.html", items = items)


if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
 