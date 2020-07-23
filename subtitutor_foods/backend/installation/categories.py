"""This module is responsible for creating the table and inserting categories."""

import mysql.connector


class InstallationCategories:
    """This class is the class of objects responsible for creating the table and inserting the categories."""

    def __init__(self):
        """Init."""
        pass

    def create_table_cat(self, cursor, cnx):
        """This method allows the creation of the category table."""
        create_table_cat = "CREATE TABLE Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB"
        cursor.execute(create_table_cat)
        cnx.commit()

    def insert_rows_cat(self, validation, cursor, cnx):
        """This method allows the insertion of categories."""
        add_cat = "INSERT INTO Categories (nom) VALUES (%s)"
        cursor.executemany(add_cat, validation.rows_cats)
        cnx.commit()
        print("Insertion catégories : ok")
