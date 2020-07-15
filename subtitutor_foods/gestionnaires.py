"""
Ce module permet de gerer les requetes de l'application vers la base de données
"""


from datetime import datetime
import mysql.connector


class Gestionnaires:
    """Cette représente la classe des objets qui permettent l'interaction de l'application à la base de données"""

    def __init__(self):
        pass

    # Categories
    def get_categories_size_page(self, taille_page_catego, page_catego, cursor, cnx):
        """ Cette méthode permet d'obtenir des pages de catégories """

        query = (
            "SELECT id, nom FROM Categories ORDER BY nom LIMIT "
            + str(taille_page_catego)
            + " OFFSET "
            + str((page_catego - 1) * taille_page_catego)
        )
        query_count = "SELECT COUNT(*) FROM Categories"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    # Favoris
    def check_in_fav(self, id_produit, id_substitut, cursor, cnx):
        """ Cette méthode permet de savoir si un favoris se trouve dans la base de données """

        query = (
            "SELECT id_produit, id_substitut FROM Favoris WHERE id_produit = "
            + str(id_produit)
            + " AND id_substitut = "
            + str(id_substitut)
        )
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    def add_in_fav(self, id_produit, id_substitut, cursor, cnx):
        """ Cette méthode permet d'ajouter un favoris dans la base de données """

        query_insert = "INSERT INTO Favoris VALUES (%s, %s, %s, %s)"
        fav_to_insert = (None, id_produit, id_substitut, datetime.now())
        cursor.execute(query_insert, fav_to_insert)
        cnx.commit()


    def get_ids_favoris_size_page(self, taille_page_favo, page_favo, cursor, cnx):
        """ Cette méthode permet d'obtenir des pages de favoris """

        query = (
            "SELECT id_produit, id_substitut, date_enregistrement FROM Favoris ORDER BY id LIMIT "
            + str(taille_page_favo)
            + " OFFSET "
            + str((page_favo - 1) * taille_page_favo)
        )
        query_count = "SELECT COUNT(*) FROM Favoris"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        result_count[0][0]
        return [result, result_count]

    def get_name_prod(self, id_produit, cursor, cnx):
        """ Cette méthode permet d'obtenir le nom d'un produit"""

        query = "SELECT id, nom FROM Produits WHERE id = " + str(id_produit)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def get_all_infos_prod(self, id_produit, cursor, cnx):
        """ Cette méthode permet d'obtenir toutes les informations d'un produit"""

        query = "SELECT * FROM Produits WHERE id = " + str(id_produit)
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    # Magasins
    def get_magasins_prod(self, nombre_magasins, id_produit, cursor, cnx):
        """ Cette méthode permet d'obtenir le magasin d'un produit """

        query = (
            "SELECT nom_magasin FROM Magasins_produits WHERE id_produit = "
            + str(id_produit)
            + " ORDER BY nom_magasin LIMIT "
            + str(nombre_magasins)
            + " OFFSET 0"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        return [result]

    # Produits
    def get_produits_size_page(
        self, category_name, taille_page_produ, page_produ, cursor, cnx
    ):
        """ Cette méthode permet d'obtenir des pages de produits """

        query = (
            "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE nom_categorie = '"
            + category_name
            + "' )"
            + " ORDER BY nom LIMIT "
            + str(taille_page_produ)
            + " OFFSET "
            + str((page_produ - 1) * taille_page_produ)
        )
        query_count = (
            "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE nom_categorie =  '"
            + category_name
            + "' )"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]

    def get_substitus_prod(
        self,
        category_name,
        produit_nutriscore,
        taille_page_subst,
        page_subst,
        cursor,
        cnx,
    ):
        """ Cette méthode permet d'obtenir des pages de substituts """

        query = (
            "SELECT id, nom, quantite, marque, nutriscore FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE nom_categorie = '"
            + category_name
            + "' ) AND  ( nutriscore <= '"
            + produit_nutriscore
            + "' )"
            + " ORDER BY nutriscore LIMIT "
            + str(taille_page_subst)
            + " OFFSET "
            + str((page_subst - 1) * taille_page_subst)
        )
        query_count = (
            "SELECT COUNT(*) FROM Produits WHERE id IN (SELECT id_produit FROM Categories_produits WHERE nom_categorie =  '"
            + category_name
            + "' ) AND  ( nutriscore <= '"
            + produit_nutriscore
            + "' )"
        )
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.execute(query_count)
        result_count = cursor.fetchall()
        return [result, result_count]
