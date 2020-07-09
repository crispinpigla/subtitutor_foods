




import mysql.connector






class InstallationMagasinsProduits:
	"""docstring for InstallationMagasinsProduits"""
	def __init__(self):
		pass


	def create_table_mag_prod(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_mag_prod = "CREATE TABLE Magasins_produits ( id_magasin VARCHAR(255), id_produit VARCHAR(255) NOT NULL ) ENGINE=INNODB"
		cursor.execute(create_table_mag_prod)
		cnx.commit()
		cursor.close()
		cnx.close()


	def insert_rows_mag_prod(self, mag_obj):

		data_mag_prod_to_insert = mag_obj.lignes_mag_prod			
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		add_mags_prod = "INSERT INTO Magasins_produits (id_magasin, id_produit) VALUES (%s, %s)"
		cursor.executemany(add_mags_prod, data_mag_prod_to_insert)
		cnx.commit()
		cursor.close()
		cnx.close()
		print('Insertion join_mag_prod : ok')











