"""This module contains the definition of the class Restaurant. 

This Module defines the Restaurant object and also contains functions to retrive data related to Restaurant class.

"""
import database_config as dc

class Restaurant():
	"""This class defines the Restaurant class. 

	This Restaurant class is used to define the Restaurant objects and all its attributes.

	Attributes:
        name: A String which the anme of the Restaurant.
        cuisine: A String which decribes the cuise being serverd at the Restaurant.
        description: A String which contains a Brief description of the Restaurant.
	"""
	def __init__(self, name, cuisine, description):
		"""Inits Restaurant with name, cuisine, description.

		"""
		self.name = name
		self.cuisine = cuisine
		self.description = description


def get_list_of_res(cnt):
	"""This function returns a List of Restaurants.

	Args:
		cnt: Count of Restuarnts that need to be returned.

	Returns:
		Returns a List of Tuples that contain the restaurant details.

	"""
	q = "select restaurant_id, name, cuisine, description from restaurant order by restaurant_id limit "+str(cnt)
	params = ()
	result = dc.selectOP(q, params)
	return result


def add_res(res):
	"""This function adds a new Restaurant to the database.

	Args:
		res: A Restaurant object that need to be added to thr database

	Returns:
		Returns a the operation outcome 1 - Success, 0 - Failure

	"""
	params = (res.name, res.cuisine, res.description,)
	q = "INSERT INTO restaurant (name, cuisine, description) VALUES (%s, %s, %s)"
	result = dc.insertOP(q, params)

	if result == 1:
		return 1
	else:
		return 0





