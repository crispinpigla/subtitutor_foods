import requests
import json



import mysql.connector



class MagasinsTables:

	"""docstring for MagasinsTables"""

	def __init__(self):
		
		self.lignes_mag = []
	

	def insert_rows_mag(self):

		data_mag_to_insert = '('

		
		request_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasins.json')
		request_mag_open_ff = json.loads(request_mag_open_ff.text)

		ligne_mag = { 'id':'', 'nom':'', 'ids_produits':'' }

		#for mag in request_mag_open_ff['tags'] :
			
		#	ligne_mag['id'] = mag['id']
		#	ligne_mag['nom'] = mag['name']
		#	ligne_mag['ids_produits'] = self.id_mag_to_ids_prods_mag(mag['id'])

		#	self.lignes_mag.append( ligne_mag )

		#	ligne_mag = { 'id':'', 'nom':'', 'ids_produits':'' }

		#	print( request_mag_open_ff['tags'].index(mag), '/', len(request_mag_open_ff['tags']) )

		for i in range(50):

			mag = request_mag_open_ff['tags'][i]
			
			ligne_mag['id'] = mag['id']
			ligne_mag['nom'] = mag['name']
			ligne_mag['ids_produits'] = self.id_mag_to_ids_prods_mag(mag['id'])

			self.lignes_mag.append( ligne_mag )

			ligne_mag = { 'id':'', 'nom':'', 'ids_produits':'' }

			print( request_mag_open_ff['tags'].index(mag), '/', len(request_mag_open_ff['tags']) )

		print( self.lignes_mag, '\n----------------' )

		for mag in self.lignes_mag :

			data_mag_to_insert += '\'' + str(mag['id']).replace( "'", "\\'") + '\' , '
			data_mag_to_insert += '\'' + str(mag['nom']).replace( "'", "\\'") + '\' , '

			if self.lignes_mag.index(mag) < ( len(self.lignes_mag) - 1 ) :
				data_mag_to_insert += '\'' + str(mag['ids_produits']).replace( "'", "\\'") + '\'' + ' ), ('
			elif self.lignes_mag.index(mag) == ( len(self.lignes_mag) - 1 ) :
				data_mag_to_insert += '\'' + str(mag['ids_produits']).replace( "'", "\\'") + '\'' + ' )'
						
			
		
		print(data_mag_to_insert)

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		add_mags = ("INSERT INTO Magasins VALUES "
   		    + data_mag_to_insert )


		print('ok 2')

		

		#cursor.execute(create_table)
		cursor.execute(add_mags)

		cnx.commit()
		cursor.close()
		cnx.close()


	def id_mag_to_ids_prods_mag(self, id_mag):
		
		page_mag = 1
		ids_prods = ''

		request_prod_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasin/magasins-u/' + str(page_mag) + '.json')
		request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)


		#while len(request_prod_mag_open_ff['products']) != 0 :
			
		#	request_prod_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasin/magasins-u/' + str(page_mag) + '.json')
		#	request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)

		#	for prod in request_prod_mag_open_ff['products']:

		#		ids_prods += '-' + request_prod_mag_open_ff['products']['code'] + '-'

		#	page_mag += 1
				

		for i in range(50):
			
			request_prod_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasin/magasins-u/' + str(page_mag) + '.json')
			request_prod_mag_open_ff = json.loads(request_prod_mag_open_ff.text)

			for prod in request_prod_mag_open_ff['products']:

				ids_prods += '-' + str(prod['code']) + '-'

			page_mag += 1

		return( ids_prods )
