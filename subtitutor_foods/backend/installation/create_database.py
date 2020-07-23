"""Docstring"""

from subtitutor_foods import config


class CreateDataBase:
	"""docstring for CreateDataBase."""
	def __init__(self):
		"""Init."""
		pass


	def create_database(self,cursor, cnx):
		"""Docs."""
		create_database = "CREATE DATABASE " + config.DATABASES_NAME + " CHARACTER SET 'utf8'"
		create_user = "CREATE USER '" + config.USER_NAME + "'@'localhost' IDENTIFIED BY '" + config.PASSEWORD + "'"
		set_privilege_user = "GRANT ALL PRIVILEGES ON " + config.DATABASES_NAME + ".* TO '" + config.USER_NAME + "'@'localhost'"
		
		cursor.execute(create_database)
		cursor.execute(create_user)
		cursor.execute(set_privilege_user)
		
		cnx.commit()
