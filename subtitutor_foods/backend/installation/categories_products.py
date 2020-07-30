"""This module is responsible for creating the table and inserting
product-categories. """


class InstallationCategoriesProducts:
    """This class is the class of objects responsible for creating the table
    and inserting the catégories-products. """

    def __init__(self):
        """Init."""
        pass

    def create_table_categories_products(self, cursor, connection):
        """This method allows the creation of the table of
        product-categories. """
        create_table_categories_products = (
            "CREATE TABLE IF NOT EXISTS Categories_produits ( nom_categorie "
            "VARCHAR(255) NOT "
            "NULL, id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB ")
        cursor.execute(create_table_categories_products)
        connection.commit()

    def insert_rows_categories_products(self, validation, cursor, connection):
        """This method allows the insertion of product-categories."""
        add_categories_products = "INSERT INTO Categories_produits (" \
                                  "id_produit, nom_categorie) VALUES (%s, %s) "
        cursor.executemany(add_categories_products,
                           validation.rows_products_categories
                           )
        connection.commit()
        print("insertion join_cat_prod : ok")
