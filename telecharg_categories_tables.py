

import requests
import json

import mysql.connector



class TelechargeCategoriesTables:
	"""docstring for Categories_Tables"""

	def __init__(self):
		
		self.colonnes_cat = []
		self.colonnes_prods = []
		self.colonnes_cat_prod = {}


	def build_rows_cat(self):
		
		request_cat_open_ff = requests.get('https://fr.openfoodfacts.org/categories/1.json')
		request_cat_open_ff = json.loads(request_cat_open_ff.text)
		compteur_cat = 0

		# Parcours des éléments de la page des catégories
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




	def url_cat_to_ids_prods(self, url):

		idsprods = []
		page_cat = 1
		request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
		request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
		end = request_prod_cat_open_ff["count"]
		id_url_prod = { 'id':'', 'url':'' , 'magasins':'' }

		# parcours de pages de la categorie
		for i in range(20):
			request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
			request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
			
			# parcours des produits de la page de categorie
			for produit in request_prod_cat_open_ff["products"] :
				idsprods.append( produit['code'] )
				id_url_prod['id'] = produit['code']
				id_url_prod['url'] = produit['url']
				#id_url_prod['magasins'] = produit['stores']
				self.colonnes_prods.append( id_url_prod )
				id_url_prod = { 'id':'', 'url':'', 'magasins':'' }
			print( 'page de la catégorie : ', page_cat )
			page_cat += 1

		return( idsprods )











