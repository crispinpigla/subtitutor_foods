"""This module is responsible for creating the table and inserting product-categories."""


import mysql.connector


class InstallationCategoriesProducts:
    """This class is the class of objects responsible for creating the table and inserting the catégories-products."""

    def __init__(self):
        """Init."""
        pass

    def create_table_cat_prod(self, cursor, cnx):
        """This method allows the creation of the table of product-categories."""
        create_table_cat_prod = "CREATE TABLE Categories_produits ( nom_categorie VARCHAR(255) NOT NULL, id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB"
        cursor.execute(create_table_cat_prod)
        cnx.commit()

    def insert_rows_cat_prod(self, validation, cursor, cnx):
        """This method allows the insertion of product-categories."""
        add_cat_prod = "INSERT INTO Categories_produits (id_produit, nom_categorie) VALUES (%s, %s)"
        cursor.executemany(add_cat_prod, validation.rows_prods_cats)
        cnx.commit()
        print("insertion join_cat_prod : ok")
