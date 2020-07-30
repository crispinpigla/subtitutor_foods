"""Application launch module."""

import json

import mysql.connector

from subtitutor_foods import config
from subtitutor_foods.backend.installation import categories
from subtitutor_foods.backend.installation import categories_products
from subtitutor_foods.backend.installation import create_database
from subtitutor_foods.backend.installation import download
from subtitutor_foods.backend.installation import favorites
from subtitutor_foods.backend.installation import products
from subtitutor_foods.backend.installation import stores
from subtitutor_foods.backend.installation import stores_products
from subtitutor_foods.backend.installation import validations
from subtitutor_foods.console import display
from subtitutor_foods.console import navigation

with open("installation_status.json", "r") as instal_stat:
    dictionnary_status = json.load(instal_stat)

if dictionnary_status["installation_status"] == "off":

    try:
        connection = mysql.connector.connect(
            user=config.USER_NAME, password=config.PASSEWORD)
        cursor = connection.cursor()
    except Exception as e:
        print(
            'Vos identifiants de connexion à la base de donnée sont '
            'incorrectes'
        )

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
    connection = create_database0.create_database(cursor, connection)
    cursor = connection.cursor()

    # Creation of tables
    installation_categories0.create_table_cat(cursor, connection)
    installation_product0.create_table_prod(cursor, connection)
    installation_stores0.create_table_store(cursor, connection)
    installation_favorites0.create_table_fav(cursor, connection)
    installation_categories_products0.create_table_cat_prod(cursor, connection)
    installation_stores_products0.create_table_store_prod(cursor, connection)

    # Inserting data into the table
    installation_categories0.insert_rows_cat(validation0, cursor, connection)
    installation_product0.insert_rows_prod(validation0, cursor, connection)
    installation_stores0.insert_rows_store(validation0, cursor, connection)
    installation_categories_products0.insert_rows_cat_prod(
        validation0, cursor, connection)
    installation_stores_products0.insert_rows_store_prod(
        validation0, cursor, connection)

    # Installation status update
    dictionnary_status["installation_status"] = "on"
    with open("installation_status.json", "w") as file:
        json.dump(dictionnary_status, file)

elif dictionnary_status["installation_status"] == "on":
    try:
        connection = mysql.connector.connect(
            user=config.USER_NAME,
            password=config.PASSEWORD,
            database=config.DATABASES_NAME
        )
        cursor = connection.cursor()
    except Exception as e:
        print('\n\nVos identifiants de connexion à la base de donnée sont '
              'incorrectes\n\n')

# Launch the application
try:
    display0 = display.Display(cursor, connection)
    my_application = navigation.Navigation(display0)
    my_application.distributor_menu()
    cursor.close()
    connection.close()
except Exception as e:
    pass
