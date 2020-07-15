"""
Ce module est chargé de la création de la table et de l'insertion des magasins
"""


import mysql.connector


class InstallationMagasins:
    """ Cette classe est la classe des objets chargés de la création de la table et de l'insertion des magasins """

    def __init__(self):
        pass

    def create_table_mag(self, cursor, cnx):
        """ Cette méthode permet la création de la table des magasins """

        create_table_mag = "CREATE TABLE Magasins (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB"
        cursor.execute(create_table_mag)
        cnx.commit()

    def insert_rows_mag(self, validation, cursor, cnx):
        """ Cette méthode permet l'insertion des magasins """

        add_mags = "INSERT INTO Magasins (nom) VALUES (%s)"
        cursor.executemany(add_mags, validation.colonnes_mags)
        cnx.commit()
        print("insertion magasins : ok")
