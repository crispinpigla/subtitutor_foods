


import mysql.connector








class MonApplication:

	"""docstring for MonApplication"""

	def __init__(self):

		#####################

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		query = ("SELECT COUNT(*) FROM Categories")
		cursor.execute(query)

		result = cursor.fetchall()

		self.lignes_cat_bd = result[0][0]


		cursor.close()
		cnx.close()

		#########################

		self.lignes_prod_cat_bd = 0

		#########################

		self.nombre_substituts = 5
		self.nombre_magasin = 5
		
		self.page_catego = 1
		self.page_produ = 1
		self.page_favo = 1

		self.taille_page_catego = 10
		self.taille_page_produ = 10
		self.taille_page_favo = 10

		self.list_catego_display = []
		self.list_produ_display = []
		self.list_favo_display = []

		self.category_cursor = {}
		self.product_cursor = {}

		self.nombr_sub = 5

	def ids_prods_to_list_ids_prod(self, str_ids_prods):
		
		output = str_ids_prods.split("--")
		output[0] = output[0][1:]
		output[-1] = output[-1][:-1]

		return(output)


	def installation_tables(self):
		

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		create_table_cat = "CREATE TABLE Categories (id VARCHAR(255) NOT NULL, nom VARCHAR(255) NOT NULL, id_produits MEDIUMTEXT, PRIMARY KEY (id) ) ENGINE=INNODB"
		create_table_prod = "CREATE TABLE Produits (id VARCHAR(255) NOT NULL,nom VARCHAR(255) NOT NULL,quantite VARCHAR(255),marque VARCHAR(255),nom_categories VARCHAR(255),labels VARCHAR(255),pays_ventes VARCHAR(255),ingredients VARCHAR(255),produits_provoqu_allergies VARCHAR(255),traces_eventuelles VARCHAR(255),nova VARCHAR(255),nutriscore VARCHAR(255),infos_nutritions TEXT ,lien_o_ff VARCHAR(255),PRIMARY KEY (id)) ENGINE=INNODB"
		create_table_mag = "CREATE TABLE Magasins (id VARCHAR(255) NOT NULL,nom VARCHAR(255) NOT NULL,id_produits MEDIUMTEXT,PRIMARY KEY (id)) ENGINE=INNODB"
		create_table_fav = "CREATE TABLE Favoris ( id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, id_produit VARCHAR(50) NOT NULL, id_resultats VARCHAR(255) NOT NULL, date_enregistrement DATETIME NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
		create_table_join_cat_prod = "CREATE TABLE Join_categories_produits ( id_categorie INT UNSIGNED NOT NULL, id_produit INT UNSIGNED NOT NULL ) ENGINE=INNODB"
		create_table_join_mag_prod = "CREATE TABLE Join_magasins_produits ( id_magasin INT UNSIGNED NOT NULL, id_produit INT UNSIGNED NOT NULL ) ENGINE=INNODB"

		cursor.execute(create_table_cat)
		cursor.execute(create_table_prod)
		cursor.execute(create_table_mag)
		cursor.execute(create_table_fav)

		cnx.commit()
		cursor.close()
		cnx.close()

	def distributeur_menu(self):

		statut = self.menu0()

		while statut != 'off' :
			entree_util = input('Entrez une sélection : ')

			##########################

			# L"application se trouve au menu 0
			if statut == 'menu0' :
				if entree_util == '1' :
					statut = self.menu1(self.taille_page_catego, self.page_catego)
				elif entree_util == '2':
					self.menu5(self.taille_page_favo, self.page_favo)
				elif entree_util == 'q':
					statut = 'off'
				else:
					statut = self.menu0()

			# L"application se trouve au menu 1
			elif statut == 'menu1':

				# sélection page suivante
				if entree_util == 's' :
					if ( self.lignes_cat_bd % self.taille_page_catego ) == 0 :
						if self.page_catego < ( self.lignes_cat_bd // self.taille_page_catego ) :
							self.page_catego += 1
							print( '------------------>   ',self.page_catego )
						statut = self.menu1(self.taille_page_catego, self.page_catego)
					elif ( self.lignes_cat_bd % self.taille_page_catego ) > 0 :
						if self.page_catego < ((self.lignes_cat_bd // self.taille_page_catego) + 1) :
							self.page_catego += 1
							print( '------------------>   ',self.page_catego )
						statut = self.menu1(self.taille_page_catego, self.page_catego)

				# sélection page précédente
				elif entree_util == 'p' :
					if self.page_catego > 1:
						self.page_catego -= 1
					statut = self.menu1(self.taille_page_catego, self.page_catego)

				# sélection menu précédent
				elif entree_util == 'mp':
					statut = self.menu0()

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				else:

					# sélection d'une catégorie
					try:
						page_ask = int(entree_util)

						list_entree_flash = []
						for cat in self.list_catego_display:
							list_entree_flash.append(cat['selection'])

						if page_ask in list_entree_flash :

							for cat in self.list_catego_display:
								if page_ask == cat['selection'] :
									self.category_cursor = cat
							#print(self.ids_prods_to_list_ids_prod(find_cat['ids_prods']))
							statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))



					# sélection non repertoriée
					except :
						
						statut = self.menu1(self.taille_page_catego, self.page_catego)


			elif statut == 'menu2':
				if entree_util == 's' :

					if ( self.lignes_prod_cat_bd % self.taille_page_produ ) == 0 :
						if self.page_produ < ( self.lignes_prod_cat_bd // self.taille_page_produ ) :
							self.page_produ += 1
							print( '------------------>   ',self.page_produ )
						statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))
					elif ( self.lignes_prod_cat_bd % self.taille_page_produ ) > 0 :
						if self.page_produ < ((self.lignes_prod_cat_bd // self.taille_page_produ) + 1) :
							self.page_produ += 1
							print( '------------------>   ',self.page_produ )
						statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))

				elif entree_util == 'p' :

					if self.page_produ > 1:
						self.page_produ -= 1
					statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))


					
				elif entree_util == 'mp':
					statut = self.menu1(self.taille_page_catego, self.page_catego)

				elif entree_util == 'q':
					statut = 'off'

				else:
					try:
						page_ask = int(entree_util)

						list_entree_flash = []
						for prod in self.list_produ_display:
							list_entree_flash.append(prod['selection'])

						if page_ask in list_entree_flash :
							for prod in self.list_produ_display:
								if page_ask == prod['selection'] :
									self.product_cursor = prod
							#statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))
							statut = self.menu3()

					except :
						statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))


			elif statut == 'menu3':
				if entree_util == 's' :
					statut = self.menu3()
				elif entree_util == 'p' :
					statut = self.menu3()
				elif entree_util == 'mp':
					statut = self.menu2(self.taille_page_produ, self.page_produ, self.ids_prods_to_list_ids_prod(self.category_cursor['ids_prods']))
				elif entree_util == 'e_r' :
					self.menu4()
				elif entree_util == 'q':
					statut = 'off'
				else:
					statut = self.menu3()

			elif statut == 'menu4':
				if entree_util == 'mp':
					self.menu3(taille_pag_sub, taille_pag_sub)
				elif entree_util == 'q':
					pass

			elif statut == 'menu5':
				if entree_util == 's' :
					self.menu5(taille_pag_fav, numero_page_fav)
				elif entree_util == 'p' :
					self.menu5(taille_pag_fav, numero_page_fav)
				elif entree_util == 'mp':
					self.menu0()
				elif entree_util == 'q':
					pass
				else:
					try:
						page_ask = int(entree_util)
						self.menu6(id_fav)
					except :
						self.menu5(taille_pag_fav, numero_page_fav)


			elif statut == 'menu6':
				if entree_util == 's' :
					pass
				elif entree_util == 'p' :
					pass
				elif entree_util == 'mp':
					self.menu5(taille_pag_fav, numero_page_fav)
				elif entree_util == 'q':
					pass
				else:
					pass

		

	def menu0(self):
		
		print( '1\n Rechercher des substituts\n--------------\n2\nConlter les favoris' )
		#entree_util = input('Entrez une sélection : ')

		#while entree_util not in ['1','2'] :
		#	print( '1\n Rechercher des substituts\n--------------\n2\nConlter les favoris' )
		#	entree_util = input('Entrez une sélection : ')

		#self.distributeur_menu('menu0', entree_util)

		return('menu0')


	def menu1(self, taille_pag_cat, numero_page_cat):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		query = ("SELECT nom, id_produits FROM Categories ORDER BY nom LIMIT " + str(self.taille_page_catego) + " OFFSET " + str((self.page_catego - 1)*self.taille_page_catego))
		cursor.execute(query)

		result = cursor.fetchall()

		self.list_catego_display = []
		catego_display = { 'selection':'' , 'nom':'' , 'ids_prods':'' }

		for i in result:

			catego_display['selection'] =  result.index(i) + ((self.page_catego-1)*self.taille_page_catego) 
			catego_display['nom'] = i[0]
			catego_display['ids_prods'] = i[1]

			self.list_catego_display.append(catego_display)
			catego_display = { 'selection':'' , 'nom':'' , 'ids_prods':'' }

			print( result.index(i) + ((self.page_catego-1)*self.taille_page_catego) , '--' ,i[0] )

		#print('liste catego display\n', self.list_catego_display )




		#print(result)

		cursor.close()
		cnx.close()

		#entree_util = input('Entrez une sélection cat : ')

		#self.distributeur_menu('menu1', entree_util)

		return('menu1')





	def menu2(self, taille_pag_prod, numero_page_prod, list_ids_prods):
		
		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		query = ("SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN " + str(tuple(list_ids_prods)) + " ORDER BY nom LIMIT " + str(taille_pag_prod) + " OFFSET " + str((numero_page_prod - 1)*taille_pag_prod ))
		query_count = ("SELECT COUNT(*) FROM Produits WHERE id IN " + str(tuple(list_ids_prods)))
		#print( 'tuuuuuuuuuuple\n', str(tuple(list_ids_prods)) )

		cursor.execute(query)
		result = cursor.fetchall()

		cursor.execute(query_count)
		result_count = cursor.fetchall()
		self.lignes_prod_cat_bd = result_count[0][0]


		self.list_produ_display = []
		prod_display = { 'selection':'', 'nutriscore':'', 'id':'' }

		for i in result:

			prod_display['selection'] = result.index(i) + ((self.page_produ-1)*self.taille_page_produ)
			prod_display['nutriscore'] = i[4]
			prod_display['id'] = i[0]

			self.list_produ_display.append(prod_display)
			prod_display = { 'selection':'', 'nutriscore':'', 'id':'' }

			print(result.index(i) + ((self.page_produ-1)*self.taille_page_produ) , '--' , i)


		cursor.close()
		cnx.close()
		return('menu2')








	def menu3(self):


		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()


		query = ("SELECT nom, quantite, marque, labels, ingredients, produits_provoqu_allergies, traces_eventuelles, nova, nutriscore, infos_nutritions FROM Produits WHERE nutriscore <= " + '\'' + self.product_cursor['nutriscore'] + '\'' + " ORDER BY nutriscore LIMIT " + str(self.nombre_substituts) + " OFFSET 0")
		query_mag = ("SELECT nom FROM Magasins WHERE id_produits LIKE '%-" + self.product_cursor['id'] + "-%'")

		#query_mag = ("SELECT nom FROM Magasins WHERE id_produits LIKE '%-" + 'a' + "-%'")
		print(query_mag)
		print(self.product_cursor['id'])



		cursor.execute(query)
		result = cursor.fetchall()

		cursor.execute(query_mag)
		result_mag = cursor.fetchall()

		mags = ''

		for i in result_mag:
			print(i)
		print('m3')


		#for i in result:

		#	print(result.index(i) , '--' , i)


		cursor.close()
		cnx.close()

		print('m3_0')

		return('menu3')











	def menu4(self):
		
		return('menu4')

	def menu5(self, arg):
		
		return('menu5')

	def menu6(self):
		
		return('menu6')

