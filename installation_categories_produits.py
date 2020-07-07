



import mysql.connector



class InstallationCategoriesProduits:
	"""docstring for InstallationCategoriesProduits"""
	def __init__(self):
		pass

	def installation_table(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_cat_prod = "CREATE TABLE Categories_produits ( id_categorie VARCHAR(255), id_produit INT ) ENGINE=INNODB"
		cursor.execute(create_table_cat_prod)
		cnx.commit()
		cursor.close()
		cnx.close()
		











