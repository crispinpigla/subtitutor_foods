








import requests
import json



request_mag_open_ff = requests.get('https://fr.openfoodfacts.org/magasins.json')
request_mag_open_ff = json.loads(request_mag_open_ff.text)




for i in request_mag_open_ff['tags']:
	print(i)



print(len(request_mag_open_ff['tags']))




