"""This module contains the definition of the class MenuItem. 

This Module defines the MenuItem object and also contains functions to retrive data related to MenuItem class.

"""

import database_config as dc

class MenuItem():
	"""This class defines the MenuItem class. 

	This MenuItem class is used to define the MenuItem objects and all its attributes.

	Attributes:
        name: A String that is a name of the Menu Item.
        course: A String which decribes the course that is Starter, main..etc.
        description: A String which contains a Brief description of the Menu Item.
        restaurant_id: A Integer which refers the Restaurant this menu Item belongs to.
	"""
	def __init__(self, name, course, description, restaurant_id):
		"""Inits MenuItem with name, course, description, restaurant_id.

		"""
		self.name = name
		self.course = course
		self.description = description
		self.restaurant_id = restaurant_id

def get_menuitems(res_id):
	"""This function returns a List of menu items for a particular Restaurant.

	Args:
		res_id: A Integer that is the unique Id of the Restaurant.

	Returns:
		Returns a List of Tuples that contain the menu items of a restaurant.

	"""
	q = "SELECT menuitem_id, name, course, description, restaurant_id FROM menuitem where restaurant_id = %s"
	params = (res_id,)
	result = dc.selectOP(q, params)

	return result

def add_menuitem(menu_item):
	"""This function adds a new Menu Item to the database.

	Args:
		res_id: A Integer that is the unique Id of the Restaurant.

	Returns:
		Returns a the operation outcome 1 - Success, 0 - Failure

	"""
	params = (menu_item.name, menu_item.course, menu_item.description, menu_item.restaurant_id)
	q = "INSERT INTO menuitem(name, course, description, restaurant_id) VALUES (%s, %s, %s, %s)"

	result = dc.insertOP(q, params)

	if result == 1:
		return 1
	else:
		return 0

def get_all_course():
	"""This function returns all the courses in the database.

	Args:
		None.

	Returns:
		Returns a List of courses in database.

	"""
	q = "SELECT course_name FROM menu_course"
	params = ()
	result = dc.selectOP(q, params)
	courses = [res[0] for res in result]

	return courses