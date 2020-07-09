



import mysql.connector



class InstallationCategoriesProduits:
	"""docstring for InstallationCategoriesProduits"""
	def __init__(self):
		pass

	def create_table_cat_prod(self):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		create_table_cat_prod = "CREATE TABLE Categories_produits ( id_categorie VARCHAR(255), id_produit VARCHAR(255) ) ENGINE=INNODB"
		cursor.execute(create_table_cat_prod)
		cnx.commit()
		cursor.close()
		cnx.close()
		

	def insert_rows_cat_prod(self, cat_obj):

		data_to_insert = []
		for cat in cat_obj.colonnes_cat_prod:
			for prod in cat_obj.colonnes_cat_prod[cat]:
				data_to_insert.append( (cat,prod) )
			print( 'build des cat_prods : ', list(cat_obj.colonnes_cat_prod).index(cat), '/', len(cat_obj.colonnes_cat_prod) )
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		data_to_insert = []
		for cat in cat_obj.colonnes_cat_prod:
			for prod in cat_obj.colonnes_cat_prod[cat]:
				data_to_insert.append( (cat,prod) )
		add_cat_prod = "INSERT INTO Categories_produits (id_categorie, id_produit) VALUES (%s, %s)"
		cursor.executemany(add_cat_prod, data_to_insert)
		cnx.commit()
		cursor.close()
		cnx.close()
		print('insertion join_cat_prod : ok')









