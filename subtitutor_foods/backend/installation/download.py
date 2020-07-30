"""This module allows you to manage the download of products."""


import json

import requests


class Download:
    """This class is the class of objects that download products."""

    def __init__(self):
        """Init."""
        self.rows_prods = []

    def get_prod_from_api(self):
        """This method downloads the data from the API."""
        for num_page in range(10):
            request_prod_api_open_ff = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&sort_by=unique_scans_n&page_size=1000&page="
                + str(num_page + 1)
                + "&json=true&fields=product_name,stores,categories,code,nutriscore_data,quantity,brands,labels,"
                  "allergens_tags,traces_tags,url,ingredients_text "
            )
            request_prod_api_open_ff = json.loads(request_prod_api_open_ff.text)
            self.rows_prods.append(request_prod_api_open_ff["products"])
            print("Téléchargement des produits ", num_page + 1, "/", 10)
