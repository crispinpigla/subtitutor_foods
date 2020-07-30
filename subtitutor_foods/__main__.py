"""Application launch module."""

import json
import mysql.connector

from subtitutor_foods.console import navigation
from subtitutor_foods.console import display
from subtitutor_foods.backend.installation import download
from subtitutor_foods.backend.installation import validations
from subtitutor_foods.backend.installation import categories
from subtitutor_foods.backend.installation import stores
from subtitutor_foods.backend.installation import products
from subtitutor_foods.backend.installation import favorites
from subtitutor_foods.backend.installation import categories_products
from subtitutor_foods.backend.installation import stores_products
from subtitutor_foods import config
from subtitutor_foods.backend.installation import create_database


with open("installation_status.json", "r") as instal_stat:
    dict_status = json.load(instal_stat)

if dict_status["installation_status"] == "off":

    try:
        cnx = mysql.connector.connect(user=config.USER_NAME, password=config.PASSEWORD)
        cursor = cnx.cursor()
    except Exception as e:
        print('Vos identifiants de connexion à la base de donnée sont incorrectes')

    # Downloading API data
    download0 = download.Download()
    download0.get_prod_from_api()

    # Construction and filtering of data to insert in the database
    validation0 = validations.Validations()
    validation0.sort_build(download0)

    # Creation of installers
    installation_categories0 = categories.InstallationCategories()
    installation_product0 = products.InstallationProducts()
    installation_stores0 = stores.InstallationStores()
    installation_favorites0 = favorites.InstallationFavorites()
    installation_categories_products0 = (
        categories_products.InstallationCategoriesProducts()
    )
    installation_stores_products0 = stores_products.InstallationStoresProducts()

    # Creation of database and update the connexion
    create_database0 = create_database.CreateDataBase()
    cnx = create_database0.create_database(cursor, cnx)
    cursor = cnx.cursor()

    # Creation of tables
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
    try:
        cnx = mysql.connector.connect(
            user=config.USER_NAME, password=config.PASSEWORD, database=config.DATABASES_NAME
        )
        cursor = cnx.cursor()
    except Exception as e:
        print('\n\nVos identifiants de connexion à la base de donnée sont incorrectes\n\n')
    


# Launch the application
try:
    disp = display.Display(cursor, cnx)
    monapp = navigation.Navigation(disp)
    monapp.distributor_menu()
    cursor.close()
    cnx.close()
except Exception as e:
    pass



