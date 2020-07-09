



import mysql.connector






class InstallationCategories:

	"""docstring for InstallationCategories"""

	def __init__(self):
		pass


	def create_table_cat(self):

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_cat = "CREATE TABLE Categories (id VARCHAR(255) NOT NULL, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
		cursor.execute(create_table_cat)
		cnx.commit()
		cursor.close()
		cnx.close()



	def insert_rows_cat(self, telech_cat):

		datas_to_insert = []
		for cat in telech_cat.colonnes_cat:
			datas_to_insert.append( ( cat['id'], cat['name'] ) )
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		add_cat = "INSERT INTO Categories VALUES (%s, %s)"
		cursor.executemany(add_cat, datas_to_insert)
		cnx.commit()
		cursor.close()
		cnx.close()
		print('Insertion catégories : ok')














