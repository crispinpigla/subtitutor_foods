import requests
import json

import mysql.connector

import categories_tables




class ProduitTables:

	"""docstring for ProduitTables"""

	def __init__(self):
		pass


	def insert_rows_prod(self, obj_cat):

		data_prod_to_insert = []

		for prod in obj_cat.colonnes_prods :
			
			request_prod_api_open_ff = requests.get('https://fr.openfoodfacts.org/api/v0/product/' + prod['id'] + '.json')
			request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)

			list_data_prod_to_insert = [ prod['id'] ]
			#data_prod_to_insert += '(' + '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['product_name']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['quantity']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['brands']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['categories']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['labels']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['countries_tags']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['ingredients_text']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['allergens_tags']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['traces_tags']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['nutriments']['nova-group_serving']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['nutriscore_data']['grade']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['nutriscore_data']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '


			list_data_prod_to_insert.append(prod['url'])
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + ', '
			

			try:
				list_data_prod_to_insert.append( str(request_prod_api_open_ff['product']['stores']) )
			except :
				list_data_prod_to_insert.append( '' )
			#data_prod_to_insert += '\'' + str(list_data_prod_to_insert[-1]).replace( "'", "\\'") + '\'' + '), '

			data_prod_to_insert.append(tuple(list_data_prod_to_insert))

			print( 'build des produits : \n',obj_cat.colonnes_prods.index(prod) , '/' , len( obj_cat.colonnes_prods )  )

		#data_prod_to_insert = data_prod_to_insert[:-2]
		#print( '---------------------   data to insert : \n', data_prod_to_insert )

		




			#print( obj_cat.colonnes_prods.index(prod) , '/' , len( obj_cat.colonnes_prods )  )

			
			#print('list_data_prod_to_insert   :    ', list_data_prod_to_insert )
			
			
			#for col in list_data_prod_to_insert:
			#	if list_data_prod_to_insert.index(col) < ( len(list_data_prod_to_insert) - 1 ) :
			#		data_prod_to_insert += '\'' + str(col).replace( "'", "\\'") + '\' , ' + str( list_data_prod_to_insert.index(col)) + '//' + str(( len(list_data_prod_to_insert)))
			#	elif list_data_prod_to_insert.index(col) == ( len(list_data_prod_to_insert) - 1 ) :

			#		if obj_cat.colonnes_prods.index(prod) < ( len(obj_cat.colonnes_prods) - 1 ) :
			#			data_prod_to_insert += '\'' + str(col).replace( "'", "\\'") + '\'' + ' ), ('
			#		elif obj_cat.colonnes_prods.index(prod) == ( len(obj_cat.colonnes_prods) - 1 ) :
			#			data_prod_to_insert += '\'' + str(col).replace( "'", "\\'") + '\' )--------'

			
		#print( data_prod_to_insert )

		cnx = mysql.connector.connect(user='p5_user', password='motdepasse', database='p5_0')
		cursor = cnx.cursor()

		add_prods = "INSERT INTO Produits VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

		#print( 'data prod to insert ----', obj_cat.colonnes_prods )

		#cursor.execute(create_table)
		cursor.executemany(add_prods, data_prod_to_insert)

		cnx.commit()
		cursor.close()
		cnx.close()

		print('Insertion des produits : ok')






		




