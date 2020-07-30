"""This module allows you to manage requests from the application to the database."""


from datetime import datetime


class Managers:
    """This represents the class of objects that allow the application to interact with the database.."""

    def __init__(self):
        """Init."""
        pass

    # Categories
    def get_categories_size_page(self, size_page_catego, page_catego, cursor, cnx):
        """This method allows you to obtain category pages."""
        query = (
            "SELECT id, nom FROM Categories ORDER BY nom LIMIT "
            + str(size_page_catego)
            + " OFFSET "
            + str((page_catego - 1) * size_page_catego)
        )
        query_count = "SELECT COUNT(*) FROM Categories"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    # Favorites
    def check_in_fav(self, id_product, id_substitute, cursor, cnx):
        """This method allows you to know if a favorite is in the database.."""
        query = (
            "SELECT id_produit, id_substitut FROM Favoris WHERE id_produit = "
            + str(id_product)
            + " AND id_substitut = "
            + str(id_substitute)
        )
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    def add_in_fav(self, id_product, id_substitute, cursor, cnx):
        """This method allows you to add a favorite in the database."""
        query_insert = "INSERT INTO Favoris VALUES (%s, %s, %s, %s)"
        fav_to_insert = (None, id_product, id_substitute, datetime.now())
        cursor.execute(query_insert, fav_to_insert)
        cnx.commit()

    def get_ids_favorites_size_page(self, size_page_favo, page_favo, cursor, cnx):
        """This method allows to obtain bookmarks pages."""
        query = (
            "SELECT id_produit, id_substitut, date_enregistrement FROM Favoris ORDER BY id LIMIT "
            + str(size_page_favo)
            + " OFFSET "
            + str((page_favo - 1) * size_page_favo)
        )
        query_count = "SELECT COUNT(*) FROM Favoris"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        result_count[0][0]
        return [result, result_count]

    def get_name_prod(self, id_product, cursor, cnx):
        """This method allows to obtain the name of a product."""
        query = "SELECT id, nom FROM Produits WHERE id = " + str(id_product)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def get_all_infos_prod(self, id_product, cursor, cnx):
        """This method allows to obtain all the information of a product."""
        query = "SELECT * FROM Produits WHERE id = " + str(id_product)
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    # Stores
    def get_stores_prod(self, stores_number, id_product, cursor, cnx):
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
        self, category_name, size_page_produ, page_produ, cursor, cnx
    ):
        """This method makes it possible to obtain product pages."""
        query = (
            "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM "
            "Categories_produits WHERE nom_categorie = '"
            + category_name
            + "' )"
            + " ORDER BY nom LIMIT "
            + str(size_page_produ)
            + " OFFSET "
            + str((page_produ - 1) * size_page_produ)
        )
        query_count = (
            "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE "
            "nom_categorie =  '"
            + category_name
            + "' )"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    def get_substitutes_prod(
        self,
        category_name,
        product_nutriscore,
        size_page_subst,
        page_subst,
        cursor,
        cnx,
    ):
        """This method makes it possible to obtain substitute pages."""
        query = (
            "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM "
            "Categories_produits WHERE nom_categorie = '"
            + category_name
            + "' ) AND  ( nutriscore < '"
            + product_nutriscore
            + "' )"
            + " ORDER BY nutriscore LIMIT "
            + str(size_page_subst)
            + " OFFSET "
            + str((page_subst - 1) * size_page_subst)
        )
        query_count = (
            "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE "
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
