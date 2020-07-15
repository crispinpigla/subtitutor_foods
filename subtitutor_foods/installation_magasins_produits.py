"""
Ce module est chargé de la création de la table et de l'insertion des magasins-produits
"""


import mysql.connector


class InstallationMagasinsProduits:
    """ Cette classe est la classe des objets chargés de la création de la table et de l'insertion des magasins-produits """

    def __init__(self):
        pass

    def create_table_mag_prod(self, cursor, cnx):
        """ Cette méthode permet la création de la table des magasins-produits """

        create_table_mag_prod = "CREATE TABLE Magasins_produits ( nom_magasin VARCHAR(255) NOT NULL, id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB"
        cursor.execute(create_table_mag_prod)
        cnx.commit()

    def insert_rows_mag_prod(self, validation, cursor, cnx):
        """ Cette méthode permet l'insertion des magasins-produits """

        add_mags_prod = (
            "INSERT INTO Magasins_produits (id_produit, nom_magasin) VALUES (%s, %s)"
        )
        cursor.executemany(add_mags_prod, validation.colonnes_prods_mags)
        cnx.commit()
        print("Insertion join_mag_prod : ok")
