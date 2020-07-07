







import mysql.connector






class InstallationFavoris:
	"""docstring for InstallationFavoris"""
	def __init__(self):
		pass

	def installation_table(self):
		

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_fav = "CREATE TABLE Favoris ( id INT UNSIGNED NOT NULL AUTO_INCREMENT, id_produit INT NOT NULL, id_resultats INT NOT NULL, date_enregistrement DATETIME NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
		cursor.execute(create_table_fav)
		cnx.commit()
		cursor.close()
		cnx.close()
		




