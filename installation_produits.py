

import mysql.connector



class InstallationProduits:
	"""docstring for InstallationProduits"""

	def __init__(self):

		pass


	def create_table_prod(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_prod = "CREATE TABLE Produits (id VARCHAR(255) NOT NULL,nom TEXT NOT NULL,quantite VARCHAR(255),marque TEXT,nom_categories TEXT,labels TEXT,pays_ventes TEXT,ingredients TEXT,produits_provoqu_allergies TEXT,traces_eventuelles TEXT,nova VARCHAR(255),nutriscore VARCHAR(255),infos_nutritions TEXT ,lien_o_ff TEXT,PRIMARY KEY (id)) ENGINE=INNODB"
		cursor.execute(create_table_prod)
		cnx.commit()
		cursor.close()
		cnx.close()
		

	def insert_rows_prod(self, tri_prd):

		prods_trie = []
		for prods in tri_prd.produits_trie :
			une_ligne = []
			for col in prods:
				une_ligne.append(prods[col])
			prods_trie.append(tuple(une_ligne))
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		add_prods = "INSERT INTO Produits VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.executemany(add_prods, prods_trie)
		cnx.commit()
		cursor.close()
		cnx.close()
		print('Insertion des produits : ok')


