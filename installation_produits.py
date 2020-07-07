

import mysql.connector



class InstallationProduits:
	"""docstring for InstallationProduits"""

	def __init__(self):
		pass


	def installation_table(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_prod = "CREATE TABLE Produits (id INT NOT NULL,nom VARCHAR(255) NOT NULL,quantite VARCHAR(255),marque VARCHAR(255),nom_categories VARCHAR(255),labels VARCHAR(255),pays_ventes VARCHAR(255),ingredients VARCHAR(255),produits_provoqu_allergies VARCHAR(255),traces_eventuelles VARCHAR(255),nova VARCHAR(255),nutriscore VARCHAR(255),infos_nutritions TEXT ,lien_o_ff VARCHAR(255),PRIMARY KEY (id)) ENGINE=INNODB"
		cursor.execute(create_table_prod)
		cnx.commit()
		cursor.close()
		cnx.close()
		


