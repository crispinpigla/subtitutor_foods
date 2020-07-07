

import requests
import json


import categories_tables
import produits_tables
import magasins_table
import favoris_table
import join_cat_prod
import join_mag_prod

import installation_categories
import installation_magasins
import installation_produits
import installation_favoris
import installation_categories_produits
import installation_magasins_produits

import monappli


installation_categories0 = installation_categories.InstallationCategories()
installation_produit0 = installation_produits.InstallationProduits()
#installation_magasins0 = installation_magasins.InstallationMagasins()
#installation_favoris0 = installation_favoris.InstallationFavoris()
#installation_categories_produits0 = installation_categories_produits.InstallationCategoriesProduits()
#installation_magasins_produits0 = installation_magasins_produits.InstallationMagasinsProduits()


"""
cat_table = categories_tables.CategoriesTables()
cat_table.build_rows_cat()
cat_table.insert_rows_cat()

prod_table = produits_tables.ProduitTables()
prod_table.insert_rows_prod(cat_table)

cat_prod_table = join_cat_prod.JoinCategorieProduitTable()
cat_prod_table.insert_rows_cat_prod(cat_table)

mag_table = magasins_table.MagasinsTables()
mag_table.build_rows_mag()
mag_table.insert_rows_mag()

mag_prod_table = join_mag_prod.JoinMagasinProduitTable()
mag_prod_table.insert_rows_mag_prod(mag_table)
"""

monapp = monappli.MonApplication()
monapp.distributeur_menu()

#-----------------------------------------------------

#request_prod_cat_open_ff = requests.get('https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux/1.json')
#request_prod_api_open_ff = requests.get('https://fr.openfoodfacts.org/api/v0/product/20842703.json')


#request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
#request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)

#monapp = monappli.MonApplication()
#monapp.installation_tables()



find = '3760159011421'


"""
for i in request_prod_cat_open_ff['products'][0] :
	if find in str(request_prod_cat_open_ff['products'][0][i]):
		print(i )
"""

#print( request_prod_api_open_ff['product']['product_name'] )


#print( len(request_prod_cat_open_ff['products'][0]) )

#print( len(request_prod_api_open_ff['product']) )






#print( request_prod_api_open_ff['product']['url'] )

"""
for i in request_prod_api_open_ff['product'] :
	if find in str(request_prod_api_open_ff['product'][i]):
		print( i, '---->', request_prod_api_open_ff['product'][i] )
"""


#print( len(request_prod_api_open_ff['product']['nutriments']) )
"""
for i0 in request_prod_api_open_ff['product']['nutriments']:
	print( i0 )
"""
