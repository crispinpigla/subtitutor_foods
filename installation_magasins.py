
import mysql.connector



class InstallationMagasins:
	"""docstring for InstallationMagasin"""

	def __init__(self):
		pass

	def create_table_mag(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_mag = "CREATE TABLE Magasins (id VARCHAR(255) NOT NULL,nom VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB"
		cursor.execute(create_table_mag)
		cnx.commit()
		cursor.close()
		cnx.close()


	def insert_rows_mag(self, telech_mag):

		# build des lignes à insérer dans les lignes de la table de jointure magasin produits
		data_mag_to_insert = []
		for mag in telech_mag.lignes_mag:
			data_mag_to_insert.append( ( mag['id'], mag['nom'] ) )
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		add_mags = "INSERT INTO Magasins VALUES (%s, %s)"
		cursor.executemany(add_mags, data_mag_to_insert)
		cnx.commit()
		cursor.close()
		cnx.close()
		print('insertion magasins : ok')


		