

import requests
import json

import mysql.connector



class CategoriesTables:
	"""docstring for Categories_Tables"""

	def __init__(self):
		
		self.colonnes_cat = []

		self.colonnes_prods = []

		self.colonnes_cat_prod = {}


	def build_rows_cat(self):
		
		request_cat_open_ff = requests.get('https://fr.openfoodfacts.org/categories/1.json')
		request_cat_open_ff = json.loads(request_cat_open_ff.text)

		compteur_cat = 0

		#print( request_cat_open_ff['tags'][48]['url'] + '/' + str(1) + '.json' )


		#for categorie in request_cat_open_ff['tags']:
			
		#	colonne = { 'id':'', 'name':'', 'url':'', 'idsprods':'' }

		#	colonne['id'] = categorie['id'] 
		#	colonne['name'] = categorie['name']
		#	colonne['url'] = categorie['url']
		#	colonne['idsprods'] = self.url_cat_to_ids_prods(colonne['url'])

		#	self.colonnes_cat.append( colonne )

		#	compteur_cat += 1
		#	print( 'compteur cat : ', compteur_cat )
			#print( colonne['url'] )

		for i in range(20):
			
			colonne = { 'id':'', 'name':'', 'url':'', 'idsprods':[] }

			colonne['id'] = request_cat_open_ff['tags'][i]['id'] 
			colonne['name'] = request_cat_open_ff['tags'][i]['name']
			colonne['url'] = request_cat_open_ff['tags'][i]['url']
			colonne['idsprods'] = self.url_cat_to_ids_prods(request_cat_open_ff['tags'][i]['url'])

			self.colonnes_cat_prod[colonne['id']] = colonne['idsprods']

			self.colonnes_cat.append( colonne )

			compteur_cat += 1
			print( 'compteur cat : ', compteur_cat )
			print('---------')

		# Unifification des produits
		colonnes_prods_flash_in = []
		colonnes_prods_flash_out = list( self.colonnes_prods )
		for prod in colonnes_prods_flash_out :
			if prod not in colonnes_prods_flash_in :
				colonnes_prods_flash_in.append(prod)
		self.colonnes_prods = colonnes_prods_flash_in

		# Listérisation du dictionnaire produit catégorie
		#for cat_prod in self.colonnes_cat_prod:
		#	self.colonnes_cat_prod[cat_prod] = self.colonnes_cat_prod[cat_prod].split('--')
		#	self.colonnes_cat_prod[cat_prod][0] = self.colonnes_cat_prod[cat_prod][0][1:]
		#	self.colonnes_cat_prod[cat_prod][-1] = self.colonnes_cat_prod[cat_prod][-1][:-1]





		#print( 'colonnes catégories : \n', self.colonnes_cat, '\n------------------------' )

		#print( 'colonnes produits : \n', self.colonnes_prods, '\n------------------------' )

		#print( 'colonnes catégories-produits : \n', self.colonnes_cat_prod, '\n------------------------' )





	def url_cat_to_ids_prods(self, url):

		idsprods = []
		page_cat = 1

		request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
		request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)

		end = request_prod_cat_open_ff["count"]

		id_url_prod = { 'id':'', 'url':'' , 'magasins':'' }

		#while len(request_prod_cat_open_ff["products"]) > 0 :

		#	request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
		#	request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
			
		#	for produit in request_prod_cat_open_ff["products"] :
		#		idsprods += '-' + produit['code'] + '-'

		#	print( request_prod_cat_open_ff["skip"] )
		#	print( request_prod_cat_open_ff["page_size"] )
		#	print( page_cat )
		#	print('---------')
		#	page_cat += 1

		# parcours de pages de la categorie
		for i in range(20):
			
			request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
			request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
			
			# parcours des produits de la page
			for produit in request_prod_cat_open_ff["products"] :
				idsprods.append( produit['code'] )

				id_url_prod['id'] = produit['code']
				id_url_prod['url'] = produit['url']
				#id_url_prod['magasins'] = produit['stores']
				self.colonnes_prods.append( id_url_prod )
				id_url_prod = { 'id':'', 'url':'', 'magasins':'' }

			#print( request_prod_cat_open_ff["skip"] )
			#print( request_prod_cat_open_ff["page_size"] )
			print( 'page de la catégorie : ', page_cat )
			page_cat += 1



		return( idsprods )







	def insert_rows_cat(self):

		datas_to_insert = []

		for cat in self.colonnes_cat:
			datas_to_insert.append( ( cat['id'], cat['name'], str(cat['idsprods']) ) )

		#print( 'données à insérer : \n', datas_to_insert )



		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()




		#create_table = "CREATE TABLE Categories (id VARCHAR(255) NOT NULL, nom VARCHAR(255) NOT NULL, id_produits MEDIUMTEXT, PRIMARY KEY (id) ) ENGINE=INNODB"
		

		add_cat = "INSERT INTO Categories VALUES (%s, %s, %s)"

		#print( add_cat, '----' )

		#cursor.execute(create_table)
		cursor.executemany(add_cat, datas_to_insert)

		cnx.commit()
		cursor.close()
		cnx.close()

		print('Insertion catégories : ok')








