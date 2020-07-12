

import requests
import json


import telecharg_categories_tables
import telecharg_produits_tables
import telecharg_magasins_table
import favoris_table


import tri_produits

import installation_categories
import installation_magasins
import installation_produits
import installation_favoris
import installation_categories_produits
import installation_magasins_produits

import monappli

"""
# Téléchargement des données de l'api
telech_cat_table = telecharg_categories_tables.TelechargeCategoriesTables()
telech_prod_table = telecharg_produits_tables.TelechargeProduitTables()
telech_mag_table = telecharg_magasins_table.TelechargeMagasinsTables()

# Constrution des données à insérer dans la base
telech_cat_table.build_rows_cat()
telech_prod_table.build_rows_prod(telech_cat_table)
telech_mag_table.build_rows_mag()

# Filtrage des produits n'ayant pas de nutriscore
tri_prod = tri_produits.TriProduits()
tri_prod.tri_prod(telech_prod_table.colonnes_prods_non_trie)

# Création des installateurs
installation_categories0 = installation_categories.InstallationCategories()
installation_produit0 = installation_produits.InstallationProduits()
installation_magasins0 = installation_magasins.InstallationMagasins()
installation_favoris0 = installation_favoris.InstallationFavoris()
installation_categories_produits0 = installation_categories_produits.InstallationCategoriesProduits()
installation_magasins_produits0 = installation_magasins_produits.InstallationMagasinsProduits()

# Création des tables
installation_categories0.create_table_cat()
installation_produit0.create_table_prod()
installation_magasins0.create_table_mag()
installation_favoris0.create_table_fav()
installation_categories_produits0.create_table_cat_prod()
installation_magasins_produits0.create_table_mag_prod()

# Insertion des données dans la table
installation_categories0.insert_rows_cat(telech_cat_table)
installation_produit0.insert_rows_prod(tri_prod)
installation_magasins0.insert_rows_mag(telech_mag_table)
installation_categories_produits0.insert_rows_cat_prod(telech_cat_table)
installation_magasins_produits0.insert_rows_mag_prod(telech_mag_table)
"""
# Lancement de l'application
monapp = monappli.MonApplication()
monapp.distributeur_menu()