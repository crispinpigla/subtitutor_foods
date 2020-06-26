

import requests
import json



class Categories_Tables:
	"""docstring for Categories_Tables"""

	def __init__(self):
		
		self.colonnes_cat = []


	def build_rows(self):
		
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

		for i in range(10):
			
			colonne = { 'id':'', 'name':'', 'url':'', 'idsprods':'' }

			colonne['id'] = request_cat_open_ff['tags'][i]['id'] 
			colonne['name'] = request_cat_open_ff['tags'][i]['name']
			colonne['url'] = request_cat_open_ff['tags'][i]['url']
			colonne['idsprods'] = self.url_cat_to_ids_prods(request_cat_open_ff['tags'][i]['url'])

			self.colonnes_cat.append( colonne )

			compteur_cat += 1
			print( 'compteur cat : ', compteur_cat )


		print( self.colonnes_cat )





	def url_cat_to_ids_prods(self, url):

		idsprods = ''
		page_cat = 1

		request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
		request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)

		end = request_prod_cat_open_ff["count"]

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

		for i in range(3):
			
			request_prod_cat_open_ff = requests.get( url + '/' + str(page_cat) + '.json' )
			request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
			
			for produit in request_prod_cat_open_ff["products"] :
				idsprods += '-' + produit['code'] + '-'

			print( request_prod_cat_open_ff["skip"] )
			print( request_prod_cat_open_ff["page_size"] )
			print( page_cat )
			print('---------')
			page_cat += 1



		return( idsprods )



