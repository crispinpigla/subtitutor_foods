
import mysql.connector



class InstallationMagasins:
	"""docstring for InstallationMagasin"""

	def __init__(self):
		pass

	def installation_table(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_mag = "CREATE TABLE Magasins (id VARCHAR(255) NOT NULL,nom VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB"
		cursor.execute(create_table_mag)
		cnx.commit()
		cursor.close()
		cnx.close()
		