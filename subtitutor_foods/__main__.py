import requests
import json
import mysql.connector

import telechargement
import validations
import installation_categories
import installation_magasins
import installation_produits
import installation_favoris
import installation_categories_produits
import installation_magasins_produits
import monappli

cnx = mysql.connector.connect(user="p5_user", password="motdepasse", database="p5_0")
cursor = cnx.cursor()

"""
# Téléchargement des données de l'api
telechargement0 = telechargement.Telechargement()
telechargement0.get_prod_from_api()

# Constrution et filtrage des données à insérer dans la base
validation0 = validations.Validations()
validation0.tri_build(telechargement0)

# Création des installateurs
installation_categories0 = installation_categories.InstallationCategories()
installation_produit0 = installation_produits.InstallationProduits()
installation_magasins0 = installation_magasins.InstallationMagasins()
installation_favoris0 = installation_favoris.InstallationFavoris()
installation_categories_produits0 = installation_categories_produits.InstallationCategoriesProduits()
installation_magasins_produits0 = installation_magasins_produits.InstallationMagasinsProduits()

# Création des tables
installation_categories0.create_table_cat(cursor,cnx)
installation_produit0.create_table_prod(cursor,cnx)
installation_magasins0.create_table_mag(cursor,cnx)
installation_favoris0.create_table_fav(cursor,cnx)
installation_categories_produits0.create_table_cat_prod(cursor,cnx)
installation_magasins_produits0.create_table_mag_prod(cursor,cnx)

# Insertion des données dans la table
installation_categories0.insert_rows_cat(validation0,cursor,cnx)
installation_produit0.insert_rows_prod(validation0,cursor,cnx)
installation_magasins0.insert_rows_mag(validation0,cursor,cnx)
installation_categories_produits0.insert_rows_cat_prod(validation0,cursor,cnx)
installation_magasins_produits0.insert_rows_mag_prod(validation0,cursor,cnx)
"""
# Lancement de l'application
monapp = monappli.MonApplication(cursor, cnx)
monapp.distributeur_menu()


cursor.close()
cnx.close()