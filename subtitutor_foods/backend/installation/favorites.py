"""This module is responsible for creating the favorites table."""


class InstallationFavorites:
    """This class is the class of objects responsible for creating the
    favorites table. """

    def __init__(self):
        """Init."""
        pass

    def create_table_favorites(self, cursor, connection):
        """This method allows the creation of the favorites table."""
        create_table_favorites = (
            "CREATE TABLE IF NOT EXISTS Favoris ( id INT UNSIGNED NOT NULL "
            "AUTO_INCREMENT, id_produit "
            "BIGINT UNSIGNED NOT NULL, id_substitut BIGINT UNSIGNED NOT "
            "NULL, date_enregistrement "
            "DATETIME NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB ")
        cursor.execute(create_table_favorites)
        connection.commit()
