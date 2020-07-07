



import mysql.connector






class InstallationCategories:
	"""docstring for InstallationCategories"""
	def __init__(self):
		pass

	def de_api_vers_appli(self):

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_cat = "CREATE TABLE Categories (id VARCHAR(255) NOT NULL, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
		cursor.execute(create_table_cat)
		cnx.commit()
		cursor.close()
		cnx.close()
		















