



import mysql.connector




class JoinMagasinProduitTable:
	"""docstring for JoinCategorieProduitTable"""

	def __init__(self):
		pass




	def insert_rows_mag_prod(self, mag_obj):


		data_mag_prod_to_insert = mag_obj.lignes_mag_prod			
		
		#print('dans mag_prod table  :\n',data_mag_prod_to_insert)

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		add_mags_prod = "INSERT INTO Join_magasins_produits (id_magasin, id_produit) VALUES (%s, %s)"

		cursor.executemany(add_mags_prod, data_mag_prod_to_insert)


		cnx.commit()
		cursor.close()
		cnx.close()

		print('Insertion join_mag_prod : ok')





