

import requests
import json

import mysql.connector



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







	def create_insert_rows(self):

		datas_to_insert = ''
		data_to_insert = ''

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()


		for cat in self.colonnes_cat:

		#	cursor.execute("INSERT INTO Categories (id, nom, id_produits) VALUES (%(id)s, %(name)s, %(idsprods)s)", cat)

			##########

			for key in cat:
				if key == 'url' :
					pass
				elif key != 'idsprods' :
					data_to_insert += '\'' + cat[key].replace( "'", "\\'") + '\'' + ', '
				elif key == 'idsprods' :
					data_to_insert += '\'' + cat[key].replace("'", "\\'") + '\''

			if self.colonnes_cat.index(cat) != ( len(self.colonnes_cat) - 1 ) :
				data_to_insert = '(' + data_to_insert + '), '
			else:
				data_to_insert = '(' + data_to_insert + ') '

			datas_to_insert += data_to_insert
			data_to_insert = ''

			##########

		create_table = "CREATE TABLE Categories (id VARCHAR(255) NOT NULL, nom VARCHAR(255) NOT NULL, id_produits MEDIUMTEXT, PRIMARY KEY (id) ) ENGINE=INNODB"
		

		add_cat = ("INSERT INTO Categories "
           		   "VALUES " + datas_to_insert )

		#print( add_cat, '----' )
		print('ok')

		

		cursor.execute(create_table)
		cursor.execute(add_cat)

		cnx.commit()
		cursor.close()
		cnx.close()


