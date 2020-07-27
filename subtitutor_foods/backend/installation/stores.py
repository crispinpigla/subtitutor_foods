"""This module is responsible for creating the table and inserting the stores."""


import mysql.connector


class InstallationStores:
    """This class is the class of objects responsible for creating the table and inserting the stores."""

    def __init__(self):
        """Init."""
        pass

    def create_table_store(self, cursor, cnx):
        """This method allows the creation of the store table."""
        create_table_store = "CREATE TABLE IF NOT EXISTS Magasins (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=INNODB"
        cursor.execute(create_table_store)
        cnx.commit()

    def insert_rows_store(self, validation, cursor, cnx):
        """This method allows the insertion of magazines."""
        add_stores = "INSERT INTO Magasins (nom) VALUES (%s)"
        cursor.executemany(add_stores, validation.rows_stores)
        cnx.commit()
        print("insertion magasins : ok")
