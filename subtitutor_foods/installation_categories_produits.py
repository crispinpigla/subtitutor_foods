"""
Ce module est chargé de la création de la table et de l'insertion des catégories-produits
"""


import mysql.connector


class InstallationCategoriesProduits:
    """ Cette classe est la classe des objets chargés de la création de la table et de l'insertion des catégories-produits """

    def __init__(self):
        pass

    def create_table_cat_prod(self, cursor, cnx):
        """ Cette méthode permet la création de la table des catégories-produits """

        create_table_cat_prod = "CREATE TABLE Categories_produits ( nom_categorie VARCHAR(255) NOT NULL, id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB"
        cursor.execute(create_table_cat_prod)
        cnx.commit()

    def insert_rows_cat_prod(self, validation, cursor, cnx):
        """ Cette méthode permet l'insertion des catégories-produits """

        add_cat_prod = "INSERT INTO Categories_produits (id_produit, nom_categorie) VALUES (%s, %s)"
        cursor.executemany(add_cat_prod, validation.colonnes_prods_cats)
        cnx.commit()
        print("insertion join_cat_prod : ok")
