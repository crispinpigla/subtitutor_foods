"""This module allows you to manage requests from the application to the
database. """

from datetime import datetime


class Managers:
    """This represents the class of objects that allow the application to
    interact with the database.. """

    def __init__(self):
        """Init."""
        pass

    # Categories
    def get_categories_size_page(
            self, size_page_categorie, page_categorie, cursor
    ):
        """This method allows you to obtain category pages."""
        query = (
                "SELECT id, nom FROM Categories ORDER BY nom LIMIT "
                + str(size_page_categorie)
                + " OFFSET "
                + str((page_categorie - 1) * size_page_categorie)
        )
        query_count = "SELECT COUNT(*) FROM Categories"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    # Favorites
    def check_in_favorites(self, id_product, id_substitute, cursor):
        """This method allows you to know if a favorite is in the database.."""
        query = (
                "SELECT id_produit, id_substitut FROM Favoris WHERE "
                "id_produit = "
                + str(id_product)
                + " AND id_substitut = "
                + str(id_substitute)
        )
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    def add_in_favorites(self, id_product, id_substitute, cursor, connection):
        """This method allows you to add a favorite in the database."""
        query_insert = "INSERT INTO Favoris VALUES (%s, %s, %s, %s)"
        favorite_to_insert = (None, id_product, id_substitute, datetime.now())
        cursor.execute(query_insert, favorite_to_insert)
        connection.commit()

    def get_ids_favorites_size_page(self, size_page_favorite, page_favorite,
                                    cursor):
        """This method allows to obtain bookmarks pages."""
        query = (
                "SELECT id_produit, id_substitut, date_enregistrement FROM "
                "Favoris ORDER BY id LIMIT "
                + str(size_page_favorite)
                + " OFFSET "
                + str((page_favorite - 1) * size_page_favorite)
        )
        query_count = "SELECT COUNT(*) FROM Favoris"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        result_count[0][0]
        return [result, result_count]

    def get_name_product(self, id_product, cursor):
        """This method allows to obtain the name of a product."""
        query = "SELECT id, nom FROM Produits WHERE id = " + str(id_product)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def get_all_information_product(self, id_product, cursor):
        """This method allows to obtain all the information of a product."""
        query = "SELECT * FROM Produits WHERE id = " + str(id_product)
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    # Stores
    def get_stores_product(self, stores_number, id_product, cursor):
        """This method allows to get the store of a product."""
        query = (
                "SELECT nom_magasin FROM Magasins_produits WHERE id_produit = "
                + str(id_product)
                + " ORDER BY nom_magasin LIMIT "
                + str(stores_number)
                + " OFFSET 0"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    # Products
    def get_products_size_page(
            self, category_name, size_page_product, page_product, cursor
    ):
        """This method makes it possible to obtain product pages."""
        query = (
                "SELECT id, nom, quantite, marque, nutriscore FROM Produits "
                "WHERE id IN (SELECT id_produit FROM "
                "Categories_produits WHERE nom_categorie = '"
                + category_name
                + "' )"
                + " ORDER BY nom LIMIT "
                + str(size_page_product)
                + " OFFSET "
                + str((page_product - 1) * size_page_product)
        )
        query_count = (
                "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT "
                "id_produit FROM Categories_produits WHERE "
                "nom_categorie =  '"
                + category_name
                + "' )"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    def get_substitutes_product(
            self,
            category_name,
            product_nutriscore,
            size_page_substute,
            page_substute,
            cursor
    ):
        """This method makes it possible to obtain substitute pages."""
        query = (
                "SELECT id, nom, quantite, marque, nutriscore FROM Produits "
                "WHERE id IN (SELECT id_produit FROM "
                "Categories_produits WHERE nom_categorie = '"
                + category_name
                + "' ) AND  ( nutriscore < '"
                + product_nutriscore
                + "' )"
                + " ORDER BY nutriscore LIMIT "
                + str(size_page_substute)
                + " OFFSET "
                + str((page_substute - 1) * size_page_substute)
        )
        query_count = (
                "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT "
                "id_produit FROM Categories_produits WHERE "
                "nom_categorie =  '"
                + category_name
                + "' ) AND  ( nutriscore < '"
                + product_nutriscore
                + "' )"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]
