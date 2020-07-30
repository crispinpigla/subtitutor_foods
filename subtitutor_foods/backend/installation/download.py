"""This module allows you to manage the download of products."""

import json

import requests


class Download:
    """This class is the class of objects that download products."""

    def __init__(self):
        """Init."""
        self.rows_products = []

    def get_products_from_api(self):
        """This method downloads the data from the API."""
        for number_page in range(10):
            request_products_api_open_food_facts = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                "&sort_by=unique_scans_n&page_size=1000&page= "
                + str(number_page + 1)
                + "&json=true&fields=product_name,stores,categories,code,"
                  "nutriscore_data,quantity,brands,labels, "
                  "allergens_tags,traces_tags,url,ingredients_text "
            )
            request_products_api_open_food_facts = json.loads(
                request_products_api_open_food_facts.text
            )
            self.rows_prods.append(
                request_products_api_open_food_facts["products"]
            )
            print("Téléchargement des produits ", number_page + 1, "/", 10)
