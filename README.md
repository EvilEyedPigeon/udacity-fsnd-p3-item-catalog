Project 2: Item Catalog
=======================

This project is a simple web application that provides a list of items within several categories.
It uses third party authentication, and logged in users can add, edit, and delete their own items.
Created using [Flask](http://flask.pocoo.org/) and [SQLAlchemy](http://www.sqlalchemy.org/).

Initial [Vagrant](https://www.vagrantup.com/) config cloned from https://github.com/udacity/fullstack-nanodegree-vm


Basic features
--------------

- JSON endpoints: get the catalog, all the items in one category, or a single item.
- Categories and items stored in a database ([PostgreSQL](http://www.postgresql.org/)).
- Third party authentication using [Google sign-in](https://developers.google.com/identity/sign-in/web/).
- All items are publicly visible. Home page shows list of categories, recent items, and all items.
- Non authenticated users can browse the catalog, but cannot make any modifications.
- Authenticated users can add, edit, and delete their own items.


Extra features
--------------

- Atom endpoint: feed with the latest items (created or updated).
- Items can have an image uploaded.
- Forms are validated using [WTForms](http://wtforms.readthedocs.org/en/latest/).
- Adding, editing, and deleting items use tokens to prevent cross-site request forgeries (CSRF).
- View user profile: logged in users can see their own profiles and list of items.


Things that would be nice / issues
----------------------------------

- Allowing creation of new categories. Currently, only a set of pre-configured categories can be used.
- Allowing the users to determine if their items are visible to public or not.
- Images are accessible to the public (as long as the user knows the file name).
- Images are never deleted and it is possible for a new uploaded image to replace an existing one (file names have the date, time, and a randomly generated UUID, so this is unlikely).


Requirements
------------

This project includes a Vagrant environment including everything necessary. To use it, install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads), and follow the project installation steps bellow.

Alternatively, you may install a [Python](http://www.python.org/), [Flask](http://flask.pocoo.org/), [SQLAlchemy](http://www.sqlalchemy.org/), and other requirements. But note that this has not been tested, and you may have to follow additional steps or make changes to some of the files. If you want to do this, look at the ```vagrant/pg_config.sh``` file (note that some of the requirements there may be for other projects).


Usage
-----

To use the project, download and configure the application. You will have to create a Google Developers Console project and use your own client ID.

Run the application:
```
$ python runserver.py
```

Then point your browser to ```localhost:5000```.


Installation
------------

After installing VirtualBox and Vagrant, do the following on the terminal:

1) Clone the project (if you don't have git, you may download the project from github).
```
$ git clone git@github.com:pt314/udacity-fsnd-p3-item-catalog.git
```

2) Start the virtual machine (the first time will take a while to download and setup things).
```
$ cd udacity-fsnd-p3-catalog/vagrant
$ vagrant up
```

3) Connect to the virtual machine.
```
$ vagrant ssh
$ cd /vagrant/catalog
```
(Use ```vagrant halt``` to turn it off.)

4) Create the database.
```
$ python database_setup.py
```

5) Populate the database.
```
$ python populate_database.py
```

This creates a set of predefined categories and sample items. You may want to edit this file to add different categories or skip adding sample items.

5) Configure Google sign-in.

A client ID is not provided. If you want to test the application, you will have to use your own client ID.

Follow the steps to create a [Google Developers Console project](https://developers.google.com/identity/sign-in/web/devconsole-project). Then go to the credentials tab and download the client ID as a JSON file. Copy the file to the ```catalog``` folder and rename it ```client_secret_google.json```.

6) Update app configuration (optional).

You may want to update the configuration in ```runserver.py``` or ```catalog/__init__.py```. Especially, you may want to ensure debug mode is disabled in ```runserver.py``` and update the secret keys in ```catalog/__init__.py```.
