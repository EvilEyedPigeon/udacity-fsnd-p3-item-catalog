from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog import db
from catalog.models import User, Category, Item


# Utility functions

def add_items(category, item_names):
	"""Add a list of items to a category."""
	for name in item_names:
		item = Item(name = name, category_id = category.id)
		db.add(item)
	db.commit()

def add_item(category, item):
    """Add an item to a category."""
    item.category_id = category.id
    db.add(item)
    db.commit()


# Sample user

user = User(name = "Peter Pan",
    email = "peter@neverlandmail.org",
    picture = "https://placehold.it/300x300.png?text=Peter+Pan")

db.add(user)
db.commit()


# Sample categories

category1 = Category(name = "Books")
db.add(category1)

category2 = Category(name = "Electronics")
db.add(category2)

category3 = Category(name = "Food")
db.add(category3)

category4 = Category(name = "Miscellaneous")
db.add(category4)

db.commit()


# Sample items

add_item(category1, Item(user = user, name = "Data Structures and Network Algorithms", description = "This is a great book!"))
add_item(category1, Item(user = user, name = "Ender's Game", description = "Did you see the movie? I only read the book."))
add_item(category1, Item(user = user, name = "Romeo and Juliet", description = "Classic love story."))

add_item(category2, Item(user = user, name = "Smart phone", description = "Pretty cool phone."))
add_item(category2, Item(user = user, name = "Tablet", description = "Who needs a computer?"))
add_item(category2, Item(user = user, name = "DVD player", description = "Sorry, no blu-ray here, but still cool :)"))

add_item(category3, Item(user = user, name = "Banana", description = "This is a yellow banana."))
add_item(category3, Item(user = user, name = "Apple", description = "This is a red apple."))
add_item(category3, Item(user = user, name = "Orange", description = "This is an orange orange."))

add_item(category4, Item(user = user, name = "Pen", description = "A pen. Pretty useful for writing notes on paper."))
add_item(category4, Item(user = user, name = "Pencil", description = "This can be pretty handy if you need to erase things you write."))
add_item(category4, Item(user = user, name = "Notepad", description = "Combined with a pen or pencil, can be used to write anything you want."))
add_item(category4, Item(user = user, name = "Playing cards", description = "Standard 52 card deck. What games do you like to play?"))
