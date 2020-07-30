"""This module is responsible for creating the table and inserting
product-stores. """


class InstallationStoresProducts:
    """This class is the class of objects responsible for creating the table
    and inserting product stores. """

    def __init__(self):
        """Init."""
        pass

    def create_table_store_product(self, cursor, connection):
        """This method allows the creation of the product-stores tables."""
        create_table_store_products = (
            "CREATE TABLE IF NOT EXISTS Magasins_produits ( nom_magasin "
            "VARCHAR(255) NOT NULL, "
            "id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB ")
        cursor.execute(create_table_store_products)
        connection.commit()

    def insert_rows_store_products(self, validation, cursor, connection):
        """This method allows the insertion of product-stores."""
        add_stores_products = (
            "INSERT INTO Magasins_produits (id_produit, nom_magasin) VALUES "
            "(%s, %s) "
        )
        cursor.executemany(add_stores_products,
                           validation.rows_products_stores)
        connection.commit()
        print("Insertion join_mag_prod : ok")
