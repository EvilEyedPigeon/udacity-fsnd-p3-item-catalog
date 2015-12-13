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

- Add image to items
- Add timestamp to items
- Show newest items
- Show message when trying to view category or item that does not exist
- Prevent CSRF using token
- Add form validation
- Cleanup Google sign-in

Done
----

- Google sign-in
- Create new item
- Edit item
- Remove item
- Add description to items

Questions
---------

- Store images in the database?

Things to keep in mind
----------------------

- Note that images are accessible to the public (as long as the user knows the file name)
- Images are never deleted

Usage
-----

- Run database_setup.py
- Run populate_database.py
- Download google client secret
  - Name it "client_secret_google.json" and place it in the catalog folder
- Run runserver.py
- Point browser to localhost:5000
