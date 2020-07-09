import requests
import json



import mysql.connector



class TelechargeMagasinsTables:

	"""docstring for MagasinsTables"""

	def __init__(self):
		
		self.lignes_mag = []
		self.lignes_mag_prod = []


	def build_rows_mag(self):
		

		request_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasins.json')
		request_mag_open_ff = json.loads(request_mag_open_ff.text)

		ligne_mag = { 'id':'', 'nom':'', 'ids_produits':[] }

		# Parcours des magasins
		for i in range(20):
			mag = request_mag_open_ff['tags'][i]
			ligne_mag['id'] = mag['id']
			ligne_mag['nom'] = mag['name']
			ligne_mag['ids_produits'] = self.url_mag_to_ids_prods_mag(mag['url'])
			self.lignes_mag.append( ligne_mag )
			ligne_mag = { 'id':'', 'nom':'', 'ids_produits':[] }
			print( 'build des magasins : \n', request_mag_open_ff['tags'].index(mag), '/', len(request_mag_open_ff['tags']) )


		# build des lignes à insérer dans les lignes de la table de jointure magasin produits
		for mag in self.lignes_mag:
			for prod in mag['ids_produits']:
				self.lignes_mag_prod.append( (mag['id'],prod) )
			print('build des mag_prods : ', self.lignes_mag.index(mag), '/', len(self.lignes_mag))


	


	def url_mag_to_ids_prods_mag(self, url_mag):
		
		page_mag = 1
		ids_prods = []
		request_prod_mag_open_ff = requests.get(url_mag + '/' + str(page_mag) + '.json')
		request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)
				
		#parcours des pages du magasin
		for i in range(20):
			request_prod_mag_open_ff = requests.get(url_mag + '/' + str(page_mag) + '.json')
			request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)

			# parcours des produits de la page de catégorie
			for prod in request_prod_mag_open_ff['products']:
				ids_prods.append(prod['code'])
			page_mag += 1
		return( ids_prods )
