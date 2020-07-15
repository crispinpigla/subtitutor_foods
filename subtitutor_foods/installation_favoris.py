"""
Ce module est chargé de la création de la table des favoris
"""

import mysql.connector


class InstallationFavoris:
    """ Cette classe est la classe des objets chargés de la création de la table des favoris """

    def __init__(self):
        pass

    def create_table_fav(self, cursor, cnx):
        """ Cette méthode permet la création de la table des favoris """

        create_table_fav = "CREATE TABLE Favoris ( id INT UNSIGNED NOT NULL AUTO_INCREMENT, id_produit BIGINT UNSIGNED NOT NULL, id_substitut BIGINT UNSIGNED NOT NULL, date_enregistrement DATETIME NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
        cursor.execute(create_table_fav)
        cnx.commit()
