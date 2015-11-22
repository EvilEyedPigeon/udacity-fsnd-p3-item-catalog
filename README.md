Project 2: Item Catalog
=======================

Web application to keep track of items and group them in categories.

Will use third party user registration and authentication. Authenticated users will have the ability to post, edit, and delete their own items.

Initial [Vagrant](https://www.vagrantup.com/) config cloned from https://github.com/udacity/fullstack-nanodegree-vm


References
----------

- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Google sign-in](https://developers.google.com/identity/sign-in/web/)


TODO
----

- Show message when trying to view category or item that does not exist
- Add, edit, and remove items
- Add Google sign-in


Usage
-----

- Run database_setup.py
- Run populate_database.py
- Download google client secret
  - Name it "client_secret_google.json" and place it in the catalog folder
- Run applycation.py
- Point browser to localhost:5000
