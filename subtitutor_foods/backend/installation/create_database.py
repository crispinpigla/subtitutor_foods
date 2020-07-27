"""This module is used to create the application database."""

from subtitutor_foods import config


class CreateDataBase:
	"""This class is the creation class of the application database."""
	def __init__(self):
		"""Init."""
		pass


	def create_database(self,cursor, cnx):
		"""This method is used to create the application database."""
		create_database = "CREATE DATABASE " + config.DATABASES_NAME + " CHARACTER SET 'utf8'"
		cursor.execute(create_database)
		cnx.commit()
