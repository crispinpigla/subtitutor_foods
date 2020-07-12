


from datetime import datetime

import mysql.connector






class GestionnaireFavoris:
	"""docstring for GestionnaireFavoris"""

	def __init__(self):
		pass

	def check_in_fav(self, id_produit, id_substitut):

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT id_produit, id_substitut FROM Favoris WHERE id_produit = '" + id_produit + "' AND id_substitut = '" + id_substitut + "' "
		cursor.execute(query)
		result = cursor.fetchall()
		cnx.commit()
		cursor.close()
		cnx.close()
		return([result])


	def add_in_fav(self, id_produit, id_substitut):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query_insert = "INSERT INTO Favoris VALUES (%s, %s, %s, %s)"
		fav_to_insert = ( None, id_produit , id_substitut, datetime.now() )
		cursor.execute(query_insert, fav_to_insert)
		cnx.commit()
		cursor.close()
		cnx.close()


	def get_ids_favoris_size_page(self, taille_page_favo, page_favo):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT id_produit, id_substitut, date_enregistrement FROM Favoris ORDER BY id LIMIT " + str(taille_page_favo) + " OFFSET " + str((page_favo - 1)*taille_page_favo)
		query_count = "SELECT COUNT(*) FROM Favoris"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.execute(query_count)
		result_count = cursor.fetchall()
		result_count[0][0]
		cursor.close()
		cnx.close()
		return([result,result_count])

	
	def get_name_prod(self, id_produit):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT id, nom FROM Produits WHERE id = " + id_produit
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		cnx.close()
		return(result)


	def get_all_infos_prod(self, id_produit):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT * FROM Produits WHERE id = '" + id_produit + "'"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		cnx.close()
		return([result])














