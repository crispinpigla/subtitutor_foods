




import mysql.connector






class InstallationMagasinsProduits:
	"""docstring for InstallationMagasinsProduits"""
	def __init__(self):
		pass


	def installation_table(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_mag_prod = "CREATE TABLE Magasins_produits ( id_magasin INT UNSIGNED NOT NULL, id_produit INT UNSIGNED NOT NULL ) ENGINE=INNODB"
		cursor.execute(create_table_mag_prod)
		cnx.commit()
		cursor.close()
		cnx.close()
		







