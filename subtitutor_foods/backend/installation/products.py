"""This module is responsible for creating the table and inserting the products."""


class InstallationProducts:
    """This class is the class of objects responsible for creating the table and inserting products."""

    def __init__(self):
        """Init."""
        pass

    def create_table_prod(self, cursor, cnx):
        """This method allows the creation of the product table."""
        create_table_prod = ("CREATE TABLE IF NOT EXISTS Produits (id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,"
                            "nom TEXT NOT NULL,quantite VARCHAR(255),marque TEXT,nom_categories TEXT,labels TEXT,"
                            "ingredients TEXT,produits_provoqu_allergies TEXT,traces_eventuelles TEXT,nutriscore "
                            "VARCHAR(255), lien_o_ff TEXT,PRIMARY KEY (id)) ENGINE=INNODB ")
        cursor.execute(create_table_prod)
        cnx.commit()

    def insert_rows_prod(self, validation, cursor, cnx):
        """This method allows the insertion of products."""
        data_to_insert = []
        for prod in validation.rows_prods:
            data_to_insert.append(
                tuple(
                    [
                        prod["code"],
                        prod["product_name"],
                        prod.get("quantity", ""),
                        prod.get("brands", ""),
                        prod.get("categories", ""),
                        prod.get("labels", ""),
                        prod.get("ingredients_text", ""),
                        str(prod.get("allergens_tags", "")),
                        str(prod.get("traces_tags", "")),
                        prod["nutriscore_data"]["grade"],
                        prod.get("url", ""),
                    ]
                )
            )
        add_prods = (
            "INSERT INTO Produits VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        cursor.executemany(add_prods, data_to_insert)
        cnx.commit()
        print("Insertion des produits : ok")
