"""Application launch module."""

import requests
import json
import mysql.connector

import Console.navigation
import Console.display
from Back_end.Installation import download
from Back_end.Installation import validations
from Back_end.Installation import installation_categories
from Back_end.Installation import installation_stores
from Back_end.Installation import installation_products
from Back_end.Installation import installation_favorites
from Back_end.Installation import installation_categories_products
from Back_end.Installation import installation_stores_products


cnx = mysql.connector.connect(user="p5_user", password="motdepasse", database="p5_0")
cursor = cnx.cursor()


with open("subtitutor_foods/installation_status.json", "r") as instal_stat:
    dict_status = json.load(instal_stat)

if dict_status["installation_status"] == "off":

    # Downloading API data
    download0 = download.Download()
    download0.get_prod_from_api()

    # Construction and filtering of data to insert in the database
    validation0 = validations.Validations()
    validation0.sort_build(download0)

    # Creation of installers
    installation_categories0 = installation_categories.InstallationCategories()
    installation_product0 = installation_products.InstallationProducts()
    installation_stores0 = installation_stores.InstallationStores()
    installation_favorites0 = installation_favorites.InstallationFavorites()
    installation_categories_products0 = (
        installation_categories_products.InstallationCategoriesProducts()
    )
    installation_stores_products0 = (
        installation_stores_products.InstallationStoresProducts()
    )

    # Création of tables
    installation_categories0.create_table_cat(cursor, cnx)
    installation_product0.create_table_prod(cursor, cnx)
    installation_stores0.create_table_store(cursor, cnx)
    installation_favorites0.create_table_fav(cursor, cnx)
    installation_categories_products0.create_table_cat_prod(cursor, cnx)
    installation_stores_products0.create_table_store_prod(cursor, cnx)

    # Inserting data into the table
    installation_categories0.insert_rows_cat(validation0, cursor, cnx)
    installation_product0.insert_rows_prod(validation0, cursor, cnx)
    installation_stores0.insert_rows_store(validation0, cursor, cnx)
    installation_categories_products0.insert_rows_cat_prod(validation0, cursor, cnx)
    installation_stores_products0.insert_rows_store_prod(validation0, cursor, cnx)

    # Installation status update
    dict_status["installation_status"] = "on"
    with open("installation_status.json", "w") as file:
        json.dump(dict_status, file)

elif dict_status["installation_status"] == "on":
    pass

# Launch the application
disp = Console.display.Display(cursor, cnx)

monapp = Console.navigation.Navigation(disp)
monapp.distributor_menu()

cursor.close()
cnx.close()
