

import gestionnaire_categories
import gestionnaire_produits
import gestionnaire_magasins
import gestionnaire_favoris




from datetime import datetime

import mysql.connector








class MonApplication:

	"""docstring for MonApplication"""

	def __init__(self):

		# les gestionnaires
		self.gest_categories = gestionnaire_categories.GestionnaireCategories()
		self.gest_produits = gestionnaire_produits.GestionnaireProduits()
		self.gest_magasins = gestionnaire_magasins.GestionnaireMagasins()
		self.gest_favoris = gestionnaire_favoris.GestionnaireFavoris()

		# lignes des elements dans la base dee donnée
		self.lignes_cat_bd = 0
		self.lignes_prod_cat_bd = 0
		self.lignes_subst_prod_cat_bd = 0
		self.lignes_fav_bd = 0

		# configurations
		self.nombre_substituts = 10
		self.nombre_magasin = 5
		
		self.page_catego = 1
		self.page_produ = 1
		self.page_subst = 1
		self.page_favo = 1

		self.taille_page_catego = 10
		self.taille_page_produ = 10
		self.taille_page_subst = 10
		self.taille_page_favo = 10

		# les élements affichés
		self.list_catego_display = []
		self.list_produ_display = []
		self.list_subst_display = []
		self.list_favo_display = []

		# les élements pointés
		self.category_cursor = {}
		self.product_cursor = {}
		self.substitut_cursor = {}
		self.favori_cursor = {}


	def distributeur_menu(self):

		# Définnition du statut de la sélection
		statut = self.menu0()

		# Boucle principale
		while statut != 'off' :

			# Entrée de l'utilisateur
			entree_util = input('\nEntrez une sélection : \n')

			# L'application se trouve au menu principal
			if statut == 'menu0' :
				if entree_util == '1' :
					statut = self.menu1()
				elif entree_util == '2':
					statut = self.menu6()
				elif entree_util == 'q':
					statut = 'off'
				else:
					statut = self.menu0()

			# L'application se trouve au menu des catégories
			elif statut == 'menu1':

				# sélection page suivante
				if entree_util == 's' :

					# Si le reste de la division du nombre de categories dans la base
					# par la taille de la page est nul alors le nombre de page des catégories
					# est la division du nombre de categories dans la base  par la taille de la page.
					# Sinon le nombre de page des catégories est (la division du nombre de categories 
					# dans la base  par la taille de la page) + 1 .
					if ( self.lignes_cat_bd % self.taille_page_catego ) == 0 :
						if self.page_catego < ( self.lignes_cat_bd // self.taille_page_catego ) :
							self.page_catego += 1
						statut = self.menu1()
					elif ( self.lignes_cat_bd % self.taille_page_catego ) > 0 :
						if self.page_catego < ((self.lignes_cat_bd // self.taille_page_catego) + 1) :
							self.page_catego += 1
						statut = self.menu1()

				# sélection page précédente
				elif entree_util == 'p' :
					if self.page_catego > 1:
						self.page_catego -= 1
					statut = self.menu1()

				# sélection menu précédent
				elif entree_util == 'mp':
					statut = self.menu0()
					self.page_catego = 1

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# sélection d'un autre choix
				else:

					# sélection d'une catégorie
					try:

						# L'élément sélectionné est un nombre
						page_ask = int(entree_util)
						list_entree_flash = []
						for cat in self.list_catego_display:
							list_entree_flash.append(cat['selection'])

						# L'élément sélectionné est un nombre des sélections affichés
						if page_ask in list_entree_flash :
							for cat in self.list_catego_display:
								if page_ask == cat['selection'] :
									self.category_cursor = cat
							statut = self.menu2()

						# L'élément sélectionné est un nombre de selections non affichées
						else:
							statut = self.menu1()

					# sélection non repertoriée
					except :
						statut = self.menu1()

			# L'application se trouve au menu des produits
			elif statut == 'menu2':

				# sélection page suivante
				if entree_util == 's' :
					if ( self.lignes_prod_cat_bd % self.taille_page_produ ) == 0 :
						if self.page_produ < ( self.lignes_prod_cat_bd // self.taille_page_produ ) :
							self.page_produ += 1
							print( '------------------>   ',self.page_produ )
						statut = self.menu2()
					elif ( self.lignes_prod_cat_bd % self.taille_page_produ ) > 0 :
						if self.page_produ < ((self.lignes_prod_cat_bd // self.taille_page_produ) + 1) :
							self.page_produ += 1
							print( '------------------>   ',self.page_produ )
						statut = self.menu2()

				# sélection page précédente
				elif entree_util == 'p' :
					if self.page_produ > 1:
						self.page_produ -= 1
					statut = self.menu2()

				# sélection menu précédent
				elif entree_util == 'mp':
					statut = self.menu1()
					self.page_produ = 1

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# sélection d'un autre choix
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
							statut = self.menu3()
						else:
							statut = self.menu2()
					except :
						statut = self.menu2()

			# L'application se trouve au menu des substituts
			elif statut == 'menu3':

				# sélection page suivante
				if entree_util == 's' :
					if ( self.lignes_subst_prod_cat_bd % self.taille_page_subst ) == 0 :
						if self.page_subst < ( self.lignes_subst_prod_cat_bd // self.taille_page_subst ) :
							self.page_subst += 1
							print( '------------------>   ',self.page_subst )
						statut = self.menu3()
					elif ( self.lignes_subst_prod_cat_bd % self.taille_page_subst ) > 0 :
						if self.page_subst < ((self.lignes_subst_prod_cat_bd // self.taille_page_subst) + 1) :
							self.page_subst += 1
							print( '------------------>   ',self.page_subst )
						statut = self.menu3()

				# sélection page précédente
				elif entree_util == 'p' :
					if self.page_subst > 1:
						self.page_subst -= 1
					statut = self.menu3()

				# sélection menu précédent
				elif entree_util == 'mp':
					statut = self.menu2()
					self.page_subst = 1

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# sélection d'une catégorie
				else:

					# sélection d'une catégorie
					try:
						page_ask = int(entree_util)

						list_entree_flash = []
						for subs in self.list_subst_display:
							list_entree_flash.append(subs['selection'])

						if page_ask in list_entree_flash :
							for subs in self.list_subst_display:
								if page_ask == subs['selection'] :
									self.substitut_cursor = subs
							statut = self.menu4()
						else:
							statut = self.menu3()

					except :
						statut = self.menu3()

			# L'application se trouve au menu de la comparaison du produit et du substitut séléctionné
			elif statut == 'menu4':

				# sélection menu précédent
				if entree_util == 'mp':
					statut = self.menu3()

				# sélection enregistrement
				elif entree_util == 'e':
					statut = self.menu5()

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# autre sélection
				else:
					statut = self.menu4()

			# L'application se trouve au menu de la confirmation des enregistrements( ou message déja enregistré )
			elif statut == 'menu5':

				# sélection du menu précédent
				if entree_util == 'mp':
					statut = self.menu4()

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# autre sélection
				else:
					statut = self.menu5()

			# L'application se trouve au menu des favoris
			elif statut == 'menu6':

				# sélection page suivante
				if entree_util == 's' :
					if ( self.lignes_fav_bd % self.taille_page_favo ) == 0 :
						if self.page_favo < ( self.lignes_fav_bd // self.taille_page_favo ):
							self.page_favo += 1
						statut = self.menu6()
					elif ( self.lignes_fav_bd % self.taille_page_favo ) > 0 :
						if self.page_favo < ((self.lignes_fav_bd // self.taille_page_favo) + 1) :
							self.page_favo += 1
						statut = self.menu6()

				# sélection page précédente
				elif entree_util == 'p' :
					if self.page_subst > 1:
						self.page_subst -= 1
					statut = self.menu6()

				# sélection du menu précédent
				elif entree_util == 'mp':
					self.page_favo = 1
					statut = self.menu0()

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# sélection d'une catégorie
				else:
					# sélection d'une catégorie
					try:
						page_ask = int(entree_util)
						list_entree_flash = []
						for fav in self.list_favo_display:
							list_entree_flash.append(fav['selection'])
						if page_ask in list_entree_flash :
							for fav in self.list_favo_display:
								if page_ask == fav['selection'] :
									self.favori_cursor = fav
									print(self.favori_cursor)
							statut = self.menu7()
						else:
							statut = self.menu6()

					except :
						statut = self.menu6()

			# L'application se trouve au menu de la comparaison du produit et du substitut enregistré
			elif statut == 'menu7':

				# sélection menu précédent
				if entree_util == 'mp':
					statut = self.menu6()

				# sélection quitter l'application
				elif entree_util == 'q':
					statut = 'off'

				# autre selection
				else:
					statut = self.menu7()



	def menu0(self):

		print('__________\nmenu0    |\n_________|')
		print( '1\n Rechercher des substituts\n--------------\n2\nConlter les favoris' )
		return('menu0')


	def menu1(self):
		
		categories = self.gest_categories.get_categories_size_page(self.taille_page_catego, self.page_catego)
		print('\n__________\nmenu1    |\n_________|\n')
		self.lignes_cat_bd = categories[1][0][0]
		self.list_catego_display = []
		catego_display = { 'selection':'' , 'id':'' ,'nom':'' , 'ids_prods':'' }
		for i in categories[0]:
			catego_display['selection'] =  categories[0].index(i) + ((self.page_catego-1)*self.taille_page_catego) 
			catego_display['id'] = i[0]
			catego_display['nom'] = i[1]
			catego_display['ids_prods'] = i[2]
			self.list_catego_display.append(catego_display)
			catego_display = { 'selection':'' , 'nom':'' , 'ids_prods':'' }
			print( categories[0].index(i) + ((self.page_catego-1)*self.taille_page_catego) , '--' ,i[1] )
		return('menu1')



	def menu2(self):

		produits = self.gest_produits.get_produits_size_page(self.category_cursor['id'], self.taille_page_produ, self.page_produ)
		self.lignes_prod_cat_bd = produits[1][0][0]
		self.list_produ_display = []
		prod_display = { 'selection':'', 'nutriscore':'', 'id':'' }
		print('__________\nmenu2    |\n_________|')
		for i in produits[0]:
			prod_display['selection'] = produits[0].index(i) + ((self.page_produ-1)*self.taille_page_produ)
			prod_display['nutriscore'] = i[4]
			prod_display['id'] = i[0]
			self.list_produ_display.append(prod_display)
			prod_display = { 'selection':'', 'nutriscore':'', 'id':'' }
			print(produits[0].index(i) + ((self.page_produ-1)*self.taille_page_produ) , '--' , i)
		return('menu2')




	def menu3(self):

		substituts = self.gest_produits.get_substitus_prod(self.category_cursor['id'], self.product_cursor['nutriscore'], self.taille_page_subst, self.page_subst)
		self.lignes_subst_prod_cat_bd = substituts[1][0][0]
		print('\n__________\nmenu3    |\n_________|\n')
		self.list_subst_display = []
		for i in substituts[0]:
			magasins = self.gest_magasins.get_magasins_prod( self.nombre_magasin, self.product_cursor['id'])
			self.list_subst_display.append( { 'selection':substituts[0].index(i) + ((self.page_produ-1)*self.taille_page_produ), 'id':i[0] } )
			print('___________________________________\n', substituts[0].index(i) + ((self.page_produ-1)*self.taille_page_produ), '\n')
			print(' substitut ---> ', i,'\n' , 'Magasins  :')
			for mag in magasins[0]:
				print(mag)
		return('menu3')





	def menu4(self):

		produits = self.gest_produits.get_informations_produits(self.substitut_cursor['id'])
		print('\n__________\nmenu4    |\n_________|\n')
		print( 'substitut_cursor : ' , self.substitut_cursor )
		print('résultat : \n')
		for info in produits[0][0]:
			print(info)
		return('menu4')





	def menu5(self):

		check_fav = self.gest_favoris.check_in_fav( self.product_cursor['id'],  self.substitut_cursor['id'])
		print('\n__________\nmenu5    |\n_________|\n')
		if check_fav[0] == []:
			self.gest_favoris.add_in_fav( self.product_cursor['id'],  self.substitut_cursor['id'])
			print('\nSubstitut enregistré dans vos favoris\n')
		else:
			print('\nCet enregistrement est déjà dans vos favoris\n')
		return('menu5')



	def menu6(self):

		favoris =  self.gest_favoris.get_ids_favoris_size_page(self.taille_page_favo, self.page_favo)
		print('\n__________\nmenu6    |\n_________|\n')
		for i in favoris[0]:
			self.list_favo_display.append( { 'selection':favoris[0].index(i) + (self.page_favo-1)*self.taille_page_favo , 'id_prod':i[0], 'id_subs':i[1] } )
			print( '________________________\nsélection  : ' , favoris[0].index(i) + ((self.page_favo-1)*self.taille_page_favo), '\n')
			produit_substitue = self.gest_favoris.get_name_prod(i[0])
			substitut = self.gest_favoris.get_name_prod(i[1])
			print(produit_substitue[0][1], '         subestitué par           ',substitut[0][1])
		return('menu6')





	def menu7(self):

		infos_prods_substitue = self.gest_favoris.get_all_infos_prod(self.favori_cursor['id_prod'])
		infos_substitut = self.gest_favoris.get_all_infos_prod(self.favori_cursor['id_subs'])
		print('\n__________\nmenu7    |\n_________|\n')
		print( 'Produit substitué :  \n', infos_prods_substitue[0][0], )
		print( 'Substitut\n', infos_substitut[0][0])
		return('menu7')

