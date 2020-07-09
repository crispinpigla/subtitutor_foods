







import mysql.connector






class InstallationFavoris:
	"""docstring for InstallationFavoris"""
	def __init__(self):
		pass

	def create_table_fav(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_fav = "CREATE TABLE Favoris ( id INT UNSIGNED NOT NULL AUTO_INCREMENT, id_produit VARCHAR(255) NOT NULL, id_substitut VARCHAR(255) NOT NULL, date_enregistrement DATETIME NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
		cursor.execute(create_table_fav)
		cnx.commit()
		cursor.close()
		cnx.close()
		




