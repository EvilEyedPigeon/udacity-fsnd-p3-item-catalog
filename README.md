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
- Show message when trying to view category or item that does not exist
- Prevent CSRF using token
- Cleanup Google sign-in
- Use blueprints to organize project

Done
----

- Google sign-in
- Create new item
- Edit item
- Remove item
- Add description to items
- Add image to items (file upload)
- Add Atom feed with recent items
- Require login to add, edit, and delete items
- Redirect to correct page after login
- Only author can edit or delete an item
- Add flash messages
- Form validation using WTForms
- View user profile (logged in user can see it's own profile)

Questions
---------

- Store images in the database?

Things to keep in mind
----------------------

- Note that images are accessible to the public (as long as the user knows the file name)
- Images are never deleted

Usage
-----

- Install Flask-WTF (WTForms)
  - https://flask-wtf.readthedocs.org/en/latest/install.html
- Run database_setup.py
- Run populate_database.py
- Download google client secret
  - Name it "client_secret_google.json" and place it in the catalog folder
- Run runserver.py
- Point browser to localhost:5000
