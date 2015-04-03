"""This module contains all the database configurations and also functions related to DB Connections

"""
import psycopg2

conn_string = "host='localhost' dbname='resmenu' user='postgres' password='Massu1774'"

def connect():
	"""This function responds with Connection Object to a database.

	Args:
		None

	Returns:
		Returns a Connection Object.

	"""
	conn = psycopg2.connect(conn_string)
	return conn

def insertOP(q, params):
	"""This function performs a INSERT operation with query provided.

	Args:
		q: A String that is an Insert query that needs to be executed.
		params: A Tuple containing the query parameters.

	Returns:
		Returns a the operation outcome 1 - Success, 0 - Failure

	"""
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute(q, params)
		conn.commit()
		conn.close()

		return 1
	except:
		return 0
	
def selectOP(q, params):
	"""This function performs a SELECT operation with query provided.

	Args:
		q: A String that is an Select query that needs to be executed.
		params: A Tuple containing the query parameters.

	Returns:
		Returns a the result set as List of Tupeles

	"""
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute(q, params)
		resultset = cursor.fetchall()

		return resultset
	except:
		return 0

