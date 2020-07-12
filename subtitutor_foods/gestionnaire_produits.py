






import mysql.connector






class GestionnaireProduits:
	"""docstring for GestionnaireFavoris"""
	def __init__(self):
		pass


	def get_produits_size_page(self, categoryid, taille_page_produ, page_produ):
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE id_categorie = '" + categoryid + "' )" + " ORDER BY nom LIMIT " + str(taille_page_produ) + " OFFSET " + str((page_produ - 1)*taille_page_produ )
		query_count = "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE id_categorie =  '" + categoryid + "' )"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.execute(query_count)
		result_count = cursor.fetchall()
		cursor.close()
		cnx.close()
		return( [result, result_count] )


	def get_substitus_prod(self, categoryid, produit_nutriscore, taille_page_subst, page_subst):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE id_categorie = '" + categoryid + "' ) AND  ( nutriscore <= '" +  produit_nutriscore + "' )" + " ORDER BY nutriscore LIMIT " + str(taille_page_subst) + " OFFSET " + str((page_subst - 1)*taille_page_subst )
		query_count = "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE id_categorie =  '" + categoryid + "' ) AND  ( nutriscore <= '" +  produit_nutriscore + "' )"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.execute(query_count)
		result_count = cursor.fetchall()
		cursor.close()
		cnx.close()
		return( [result, result_count] )


	def get_informations_produits(self, id_produit):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT * FROM Produits WHERE id = '" + id_produit + "'"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		cnx.close()
		return( [result] )










