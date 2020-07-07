



import mysql.connector






class JoinCategorieProduitTable:
	"""docstring for JoinCategorieProduitTable"""

	def __init__(self):
		pass



	def insert_rows_cat_prod(self, cat_obj):

		data_to_insert = []

		for cat in cat_obj.colonnes_cat_prod:
			for prod in cat_obj.colonnes_cat_prod[cat]:
				data_to_insert.append( (cat,prod) )
			print( 'build des cat_prods : ', list(cat_obj.colonnes_cat_prod).index(cat), '/', len(cat_obj.colonnes_cat_prod) )

		#print( 'données à insérer :\n', data_to_insert )




		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()


		data_to_insert = []

		for cat in cat_obj.colonnes_cat_prod:
			for prod in cat_obj.colonnes_cat_prod[cat]:
				data_to_insert.append( (cat,prod) )

		#print( 'données à insérer :\n', data_to_insert )


		add_cat_prod = "INSERT INTO Join_categories_produits (id_categorie, id_produit) VALUES (%s, %s)"


		cursor.executemany(add_cat_prod, data_to_insert)
		

		cnx.commit()
		cursor.close()
		cnx.close()

		print('insertion join_cat_prod : ok')
		

		
		




