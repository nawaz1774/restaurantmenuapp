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

def get_res_name_with_id(res_id):
	"""This function returns the name of the Restaurant.

	Args:
		res_id: An integer which is a restaurant id that needs to be deleted.

	Returns:
		Returns a string that contain the restaurant name.

	"""
	params = (res_id,)
	q = "select restaurant_id, name, cuisine, description from restaurant where restaurant_id = %s"
	result = dc.selectOP(q, params)
	res_name = result[0][1]

	return res_name

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

def delete_res(res_id):
	"""This function deletes a Restaurant from the database.

	Args:
		res_id: An integer which is a restaurant id that needs to be deleted.

	Returns:
		Returns a the operation outcome 1 - Success, 0 - Failure

	"""
	params = (res_id,)
	q1 = "DELETE FROM menuitem WHERE restaurant_id = %s"
	q = "DELETE FROM restaurant WHERE restaurant_id = %s"

	result1 = dc.deleteOP(q1, params)
	result = dc.deleteOP(q, params)
	print(result)
	if result == 1 and result1 == 1:
		return 1
	else:
		return 0



