"""
Ce module permet de gérer le téléchargement des produits
"""


import requests
import json

import mysql.connector


class Telechargement:
    """ Cette classe est la classe des objets qui effectuent le téléchargement des produits """

    def __init__(self):
        self.colonnes_prods = []

    def get_prod_from_api(self):
        """ Cette méthode permet de télécharger les données de l'api """

        for num_page in range(10):
            request_prod_api_open_ff = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&sort_by=unique_scans_n&page_size=1000&page="
                + str(num_page + 1)
                + "&json=true&fields=product_name,stores,categories,code,nutriscore_data,quantity,brands,labels,allergens_tags,traces_tags,url,ingredients_text"
            )
            request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)
            self.colonnes_prods.append(request_prod_api_open_ff["products"])
            print(num_page + 1)
