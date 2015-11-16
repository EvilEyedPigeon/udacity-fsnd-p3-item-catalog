from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, Category, Item

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Utility functions

def add_items(category, item_names):
	"""Add a list of items to a category."""
	for name in item_names:
		item = Item(name = name, category_id = category.id)
		session.add(item)
	session.commit()


# Sample categories

category1 = Category(name = "Books")
session.add(category1)

category2 = Category(name = "Electronics")
session.add(category2)

category3 = Category(name = "Food")
session.add(category3)

category4 = Category(name = "Miscellaneous")
session.add(category4)

session.commit()


# Sample items

item1_names = ["Data Structures and Network Algorithms", "Ender's Game", "Romeo and Juliet"]
add_items(category1, item1_names)

item2_names = ["Smart phone", "Tablet", "Laptop", "DVD player"]
add_items(category2, item2_names)

item3_names = ["Yellow banana", "Red apple", "Blue berry", "Orange orange"]
add_items(category3, item3_names)

item4_names = ["Pen", "Pencil", "Notepad", "Playing cards"]
add_items(category4, item4_names)
