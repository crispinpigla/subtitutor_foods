"""This module is responsible for creating the table and inserting product-stores."""


class InstallationStoresProducts:
    """This class is the class of objects responsible for creating the table and inserting product stores."""

    def __init__(self):
        """Init."""
        pass

    def create_table_store_prod(self, cursor, cnx):
        """This method allows the creation of the product-stores tables."""
        create_table_store_prod = ("CREATE TABLE IF NOT EXISTS Magasins_produits ( nom_magasin VARCHAR(255) NOT NULL, "
                                  "id_produit BIGINT UNSIGNED NOT NULL ) ENGINE=INNODB ")
        cursor.execute(create_table_store_prod)
        cnx.commit()

    def insert_rows_store_prod(self, validation, cursor, cnx):
        """This method allows the insertion of product-stores."""
        add_stores_prod = (
            "INSERT INTO Magasins_produits (id_produit, nom_magasin) VALUES (%s, %s)"
        )
        cursor.executemany(add_stores_prod, validation.rows_prods_stores)
        cnx.commit()
        print("Insertion join_mag_prod : ok")
