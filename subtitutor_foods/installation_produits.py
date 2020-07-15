"""
Ce module est chargé de la création de la table et de l'insertion des produits
"""


import mysql.connector


class InstallationProduits:
    """ Cette classe est la classe des objets chargés de la création de la table et de l'insertion des produits """

    def __init__(self):
        pass

    def create_table_prod(self, cursor, cnx):
        """ Cette méthode permet la création de la table des produits """

        create_table_prod = "CREATE TABLE Produits (id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,nom TEXT NOT NULL,quantite VARCHAR(255),marque TEXT,nom_categories TEXT,labels TEXT,ingredients TEXT,produits_provoqu_allergies TEXT,traces_eventuelles TEXT,nutriscore VARCHAR(255), lien_o_ff TEXT,PRIMARY KEY (id)) ENGINE=INNODB"
        cursor.execute(create_table_prod)
        cnx.commit()

    def insert_rows_prod(self, validation, cursor, cnx):
        """ Cette méthode permet l'insertion des produits """

        data_to_insert = []
        for prod in validation.colonnes_prods:
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
