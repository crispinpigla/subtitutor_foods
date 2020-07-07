



import mysql.connector




class GestionnaireCategories:
	
	"""docstring for GestionnaireFavoris"""

	def __init__(self):
		pass


	def get_categories_size_page(self, taille_page_catego, page_catego):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = ("SELECT id, nom, id_produits FROM Categories ORDER BY nom LIMIT " + str(taille_page_catego) + " OFFSET " + str((page_catego - 1)*taille_page_catego))
		query_count = ("SELECT COUNT(*) FROM Categories")
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.execute(query_count)
		result_count = cursor.fetchall()
		cursor.close()
		cnx.close()
		return( [result, result_count] )
		









