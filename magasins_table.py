import requests
import json



import mysql.connector



class MagasinsTables:

	"""docstring for MagasinsTables"""

	def __init__(self):
		
		self.lignes_mag = []
		self.lignes_mag_prod = []


	def build_rows_mag(self):
		
		#data_mag_prod_to_insert = []
		data_mag_to_insert = []

		
		request_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasins.json')
		request_mag_open_ff = json.loads(request_mag_open_ff.text)

		ligne_mag = { 'id':'', 'nom':'', 'ids_produits':[] }

		#for mag in request_mag_open_ff['tags'] :
			
		#	ligne_mag['id'] = mag['id']
		#	ligne_mag['nom'] = mag['name']
		#	ligne_mag['ids_produits'] = self.url_mag_to_ids_prods_mag(mag['id'])

		#	self.lignes_mag.append( ligne_mag )

		#	ligne_mag = { 'id':'', 'nom':'', 'ids_produits':'' }

		#	print( request_mag_open_ff['tags'].index(mag), '/', len(request_mag_open_ff['tags']) )

		for i in range(20):

			mag = request_mag_open_ff['tags'][i]
			
			ligne_mag['id'] = mag['id']
			ligne_mag['nom'] = mag['name']
			ligne_mag['ids_produits'] = self.url_mag_to_ids_prods_mag(mag['url'])

			self.lignes_mag.append( ligne_mag )

			ligne_mag = { 'id':'', 'nom':'', 'ids_produits':[] }

			print( 'build des magasins : \n', request_mag_open_ff['tags'].index(mag), '/', len(request_mag_open_ff['tags']) )

		#print( self.lignes_mag, '\n----------------' )

		# build des mag_prods
		for mag in self.lignes_mag:
			data_mag_to_insert.append( ( mag['id'], mag['nom'], str(mag['ids_produits']) ) )
			for prod in mag['ids_produits']:
				self.lignes_mag_prod.append( (mag['id'],prod) )
			print('build des mag_prods : ', self.lignes_mag.index(mag), '/', len(self.lignes_mag))


		self.lignes_mag = data_mag_to_insert	
			
		
		#print(self.lignes_mag_prod)
	

	def insert_rows_mag(self):


		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		add_mags = "INSERT INTO Magasins VALUES (%s, %s, %s)"
		#add_mags_prod = "INSERT INTO Join_magasins_produits (id_magasin, id_produit) VALUES (%s, %s)"

		#cursor.execute(create_table)

		cursor.executemany(add_mags, self.lignes_mag)
		#cursor.executemany(add_mags_prod, data_mag_prod_to_insert)


		cnx.commit()
		cursor.close()
		cnx.close()

		print('insertion magasins : ok')


	def url_mag_to_ids_prods_mag(self, url_mag):
		
		page_mag = 1
		ids_prods = []

		request_prod_mag_open_ff = requests.get(url_mag + '/' + str(page_mag) + '.json')
		request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)


		#while len(request_prod_mag_open_ff['products']) != 0 :
			
		#	request_prod_mag_open_ff = requests.get(url_mag + '/' + str(page_mag) + '.json')
		#	request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)

		#	for prod in request_prod_mag_open_ff['products']:

		#		ids_prods += '-' + request_prod_mag_open_ff['products']['code'] + '-'

		#	page_mag += 1
				
		#parcours des pages
		for i in range(20):
			
			request_prod_mag_open_ff = requests.get(url_mag + '/' + str(page_mag) + '.json')
			request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)

			# parcours des produits de la page de catégorie
			for prod in request_prod_mag_open_ff['products']:
				ids_prods.append(str(prod['code']))

			page_mag += 1

		return( ids_prods )
