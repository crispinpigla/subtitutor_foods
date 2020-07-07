



import mysql.connector






class GestionnaireMagasins:
	"""docstring for GestionnaireFavoris"""
	def __init__(self):
		pass


	def get_magasins_prod(self, nombre_magasins, id_produit):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()
		query = "SELECT nom FROM Magasins WHERE id IN (SELECT id_magasin FROM Join_magasins_produits WHERE id_produit = '" + id_produit + "' )" + " ORDER BY nom LIMIT " + str(nombre_magasins) + " OFFSET 0"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		cnx.close()
		return( [result] )
		


