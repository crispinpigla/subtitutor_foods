"""This module is responsible for creating the table and inserting the
products. """

import pdb


class InstallationProducts:
    """This class is the class of objects responsible for creating the table
    and inserting products. """

    def __init__(self):
        """Init."""
        pass

    def create_table_products(self, cursor, connection):
        """This method allows the creation of the product table."""
        create_table_products = ("CREATE TABLE IF NOT EXISTS Produits (id "
                                 "BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, "
                                 "nom TEXT NOT NULL,quantite VARCHAR(255),"
                                 "marque TEXT,nom_categories TEXT,labels "
                                 "TEXT, "
                                 "ingredients TEXT,"
                                 "produits_provoqu_allergies TEXT,"
                                 "traces_eventuelles TEXT,nutriscore "
                                 "VARCHAR(255), lien_o_ff TEXT,PRIMARY KEY ("
                                 "id)) ENGINE=INNODB ")
        cursor.execute(create_table_products)
        connection.commit()

    def insert_rows_product(self, validation, cursor, connection):
        """This method allows the insertion of products."""
        data_to_insert = []
        for product in validation.rows_products:
            data_to_insert.append(
                tuple(
                    [
                        product["code"],
                        product["product_name"].encode('ascii', errors='ignore'),
                        product.get("quantity", "").encode('ascii', errors='ignore'),
                        product.get("brands", "").encode('ascii', errors='ignore'),
                        product.get("categories", "").encode('ascii', errors='ignore'),
                        product.get("labels", "").encode('ascii', errors='ignore'),
                        product.get("ingredients_text", "").encode('ascii', errors='ignore'),
                        str(product.get("allergens_tags", "")).encode('ascii', errors='ignore'),
                        str(product.get("traces_tags", "")).encode('ascii', errors='ignore'),
                        product["nutriscore_data"]["grade"],
                        product.get("url", ""),
                    ]
                )
            )

        # pdb.set_trace()
        add_products = (
            "INSERT INTO Produits VALUES (%s, %s, %s, %s, %s, %s, %s, %s, "
            "%s, %s, %s) "
        )
        cursor.executemany(add_products, data_to_insert)
        connection.commit()
        print("Insertion des produits : ok")
