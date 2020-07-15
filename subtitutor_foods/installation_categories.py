"""
Ce module est chargé de la création de la table et de l'insertion des catégories
"""

import mysql.connector


class InstallationCategories:
    """ Cette classe est la classe des objets chargés de la création de la table et de l'insertion des catégories """

    def __init__(self):
        pass

    def create_table_cat(self, cursor, cnx):
        """ Cette méthode permet la création de la table des catégories """

        create_table_cat = "CREATE TABLE Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
        cursor.execute(create_table_cat)
        cnx.commit()

    def insert_rows_cat(self, validation, cursor, cnx):
        """ Cette méthode permet l'insertion des catégories """

        add_cat = "INSERT INTO Categories (nom) VALUES (%s)"
        cursor.executemany(add_cat, validation.colonnes_cats)
        cnx.commit()
        print("Insertion catégories : ok")
