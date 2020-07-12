import requests
import json

import mysql.connector

import telecharg_categories_tables




class TelechargeProduitTables:

	"""docstring for ProduitTables"""

	def __init__(self):
		
		self.colonnes_prods_non_trie = []




	def build_rows_prod(self, obj_cat):

		self.colonnes_prods_non_trie = []
		
		for prod in obj_cat.colonnes_prods :
			
			request_prod_api_open_ff = requests.get('https://fr.openfoodfacts.org/api/v0/product/' + prod['id'] + '.json')
			request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)

			list_data_prod_to_insert = { 'id':prod['id'] }
			
			try:
				list_data_prod_to_insert['nom'] = str(request_prod_api_open_ff['product']['product_name'])
			except :
				list_data_prod_to_insert['nom'] = ''
			
			try:
				list_data_prod_to_insert['quantite'] = str(request_prod_api_open_ff['product']['quantity']) 
			except :
				list_data_prod_to_insert['quantite'] = ''
			
			try:
				list_data_prod_to_insert['marque'] = str(request_prod_api_open_ff['product']['brands'])
			except :
				list_data_prod_to_insert['marque'] = ''
			
			try:
				list_data_prod_to_insert['categorie'] = str(request_prod_api_open_ff['product']['categories'])
			except :
				list_data_prod_to_insert['categorie'] = ''
			
			try:
				list_data_prod_to_insert['label'] = str(request_prod_api_open_ff['product']['labels'])
			except :
				list_data_prod_to_insert['label'] = ''
			
			try:
				list_data_prod_to_insert['pays'] = str(request_prod_api_open_ff['product']['countries_tags'])
			except :
				list_data_prod_to_insert['pays'] = ''
			
			try:
				list_data_prod_to_insert['ingredients'] = str(request_prod_api_open_ff['product']['ingredients_text'])
			except :
				list_data_prod_to_insert['ingredients'] = ''
			
			try:
				list_data_prod_to_insert['allergens'] = str(request_prod_api_open_ff['product']['allergens_tags'])
			except :
				list_data_prod_to_insert['allergens'] = ''
			
			try:
				list_data_prod_to_insert['traces'] = str(request_prod_api_open_ff['product']['traces_tags'])
			except :
				list_data_prod_to_insert['traces'] = ''
			
			try:
				list_data_prod_to_insert['nova'] = str(request_prod_api_open_ff['product']['nutriments']['nova-group_serving'])
			except :
				list_data_prod_to_insert['nova'] = ''
			
			try:
				list_data_prod_to_insert['nutriscore'] = str(request_prod_api_open_ff['product']['nutriscore_data']['grade'])
			except :
				list_data_prod_to_insert['nutriscore'] = ''
			
			try:
				list_data_prod_to_insert['nutriscore_data'] = str(request_prod_api_open_ff['product']['nutriscore_data'])
			except :
				list_data_prod_to_insert['nutriscore_data'] = ''
			
			list_data_prod_to_insert['url'] = prod['url']
			
			self.colonnes_prods_non_trie.append(list_data_prod_to_insert)

			print( 'build des produits : \n',obj_cat.colonnes_prods.index(prod) , '/' , len( obj_cat.colonnes_prods )  )



