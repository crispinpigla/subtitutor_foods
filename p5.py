

import requests
import json


import categories_tables

#cat_table = categories_tables.Categories_Tables()
#cat_table.build_rows()
#cat_table.create_insert_rows()


request_prod_cat_open_ff = requests.get('https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux/1.json')
#request_prod_api_open_ff = requests.get('https://fr.openfoodfacts.org/api/v0/product/20842703.json')


request_prod_cat_open_ff = json.loads(request_prod_cat_open_ff.text)
#request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)





find = '3760159011421'



for i in request_prod_cat_open_ff['products'][0] :
	if find in str(request_prod_cat_open_ff['products'][0][i]):
		print(i )



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
