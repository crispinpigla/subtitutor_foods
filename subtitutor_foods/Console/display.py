"""This module manages the display of the different menus."""

from Back_end.manager import manager
import config


class Display:
    """This class is the class of objects capable of generating displays.."""

    def __init__(self, curs, cnx):
        """Init."""
        # Relating to the connection to the database
        self.cursor = curs
        self.connection = cnx

        # the manager
        self.manage = manager.Managers()

    def menu0(self):
        """This method controls the display of the main menu."""
        print(
            "_______________________________________________\nMenu principal     \n_______________________________________________"
        )
        print(
            "1\n\nRechercher des substitutes\n---------------------------\n2\n\nConsulter les favorites\n---------------------------"
        )
        print(
            "-----------------------------------------------\nq : Quitter l'application\n-----------------------------------------------"
        )
        return "menu0"

    def menu1(self, page_catego, size_page_catego):
        """This method manages the display of the category menu."""
        categories = self.manage.get_categories_size_page(
            size_page_catego, page_catego, self.cursor, self.connection
        )
        print(
            "_______________________________________________\nMenu des catégories     \n_______________________________________________"
        )
        lines_cat_db = categories[1][0][0]
        list_catego_display = []
        catego_display = {"selection": "", "id": "", "nom": "", "ids_prods": ""}
        for i in categories[0]:
            catego_display["selection"] = categories[0].index(i) + (
                (page_catego - 1) * size_page_catego
            )
            catego_display["id"] = i[0]
            catego_display["nom"] = i[1]
            list_catego_display.append(catego_display)
            catego_display = {"selection": "", "nom": "", "ids_prods": ""}
            print(
                categories[0].index(i) + ((page_catego - 1) * size_page_catego),
                "--",
                i[1],
            )
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent  |  s : Page suivante  |  p : Page précédente\n-----------------------------------------------"
        )
        return ["menu1", lines_cat_db, list_catego_display]

    def menu2(self, page_produ, size_page_produ, category_cursor):
        """This method manages the display of the products menu."""
        products = self.manage.get_products_size_page(
            category_cursor["nom"],
            size_page_produ,
            page_produ,
            self.cursor,
            self.connection,
        )
        lines_prod_cat_bd = products[1][0][0]
        list_produ_display = []
        prod_display = {"selection": "", "nutriscore": "", "id": ""}
        print(
            "_______________________________________________\nMenu des produits     \n_______________________________________________"
        )
        for i in products[0]:
            prod_display["selection"] = products[0].index(i) + (
                (page_produ - 1) * size_page_produ
            )
            prod_display["nutriscore"] = i[4]
            prod_display["id"] = i[0]
            list_produ_display.append(prod_display)
            prod_display = {"selection": "", "nutriscore": "", "id": ""}
            print(products[0].index(i) + ((page_produ - 1) * size_page_produ))
            print("Nom :", i[1])
            print("Quantité :", i[2])
            print("Marque :", i[3])
            print("Nutriscore :", i[4])
            print("---------------------------")
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent  |  s : Page suivante  |  p : Page précédente\n-----------------------------------------------"
        )
        return ["menu2", lines_prod_cat_bd, list_produ_display]

    def menu3(
        self,
        category_cursor,
        product_cursor,
        size_page_subst,
        page_subst,
        store_numbers,
    ):
        """This method manages the display of the substitutes menu."""
        substitutes = self.manage.get_substitutes_prod(
            category_cursor["nom"],
            product_cursor["nutriscore"],
            size_page_subst,
            page_subst,
            self.cursor,
            self.connection,
        )
        lines_subst_prod_cat_db = substitutes[1][0][0]
        print(
            "_______________________________________________\nMenu des substituts     \n_______________________________________________"
        )
        list_subst_display = []
        for i in substitutes[0]:
            stores = self.manage.get_stores_prod(
                store_numbers, i[0], self.cursor, self.connection
            )
            list_subst_display.append(
                {
                    "selection": substitutes[0].index(i)
                    + ((page_subst - 1) * size_page_subst),
                    "id": i[0],
                }
            )
            print(substitutes[0].index(i) + ((page_subst - 1) * size_page_subst))
            print("Nom :", i[1])
            print("Quantité :", i[2])
            print("Marque :", i[3])
            print("Nutriscore :", i[4])
            stor_display = ""
            for stor in stores[0]:
                stor_display += stor[0] + ", "
            stor_display = stor_display[:-2]
            print("Magasin  : ", stor_display)
            print("---------------------------")
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent  |  s : Page suivante  |  p : Page précédente\n-----------------------------------------------"
        )
        return ["menu3", lines_subst_prod_cat_db, list_subst_display]

    def menu4(self, substitute_cursor, store_numbers):
        """This method manages the display of the substitute menu."""
        products = self.manage.get_all_infos_prod(
            substitute_cursor["id"], self.cursor, self.connection
        )
        print(
            "_______________________________________________\nDétails du substitut     \n_______________________________________________"
        )
        print("Nom :", products[0][0][1])
        print("Quantité :", products[0][0][2])
        print("Marque :", products[0][0][3])
        print("Catégories :", products[0][0][4])
        print("Labels :", products[0][0][5])
        print("Ingrédients :", products[0][0][6])
        allergens_display = ""
        for allerg in products[0][0][7][1:-1].split(","):
            if allerg[0] == " ":
                allerg = allerg[1:]
            allergens_display += allerg[4:-1] + ", "
        allergens_display = allergens_display[:-2]
        print("Allergènes :", allergens_display)
        traces_display = ""
        for trace in products[0][0][8][1:-1].split(","):
            if trace[0] == " ":
                trace = trace[1:]
            traces_display += trace[4:-1] + ", "
        traces_display = traces_display[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de traces :",
            traces_display,
        )
        print("Nutriscore :", products[0][0][9])
        print("Lien Open Foods Facts :", products[0][0][10])
        stores = self.manage.get_stores_prod(
            store_numbers, substitute_cursor["id"], self.cursor, self.connection
        )
        stor_display = ""
        for stor in stores[0]:
            stor_display += stor[0] + ", "
        stor_display = stor_display[:-2]
        print("Magasin  : ", stor_display)
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent  |  e : Enregistrer le substitut\n-----------------------------------------------"
        )
        return ["menu4"]

    def menu5(self, product_cursor, substitute_cursor):
        """This method manages the display of the registration confirmation menu in the database."""
        check_fav = self.manage.check_in_fav(
            product_cursor["id"], substitute_cursor["id"], self.cursor, self.connection
        )
        print(
            "_______________________________________________\nMenu d'enregistrement     \n_______________________________________________"
        )
        if check_fav[0] == []:
            self.manage.add_in_fav(
                product_cursor["id"],
                substitute_cursor["id"],
                self.cursor,
                self.connection,
            )
            print("\nSubstitut enregistré dans vos favorites\n")
        else:
            print("\nCet enregistrement est déjà dans vos favorites\n")
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent\n-----------------------------------------------"
        )
        return "menu5"

    def menu6(self, size_page_favo, page_favo):
        """This method manages the display of the favorites menu."""
        favorites = self.manage.get_ids_favorites_size_page(
            size_page_favo, page_favo, self.cursor, self.connection
        )
        print(
            "_______________________________________________\nMenu des favoris     \n_______________________________________________"
        )
        list_favo_display = []
        for i in favorites[0]:
            list_favo_display.append(
                {
                    "selection": favorites[0].index(i)
                    + (page_favo - 1) * size_page_favo,
                    "id_prod": i[0],
                    "id_subs": i[1],
                }
            )
            print(favorites[0].index(i) + ((page_favo - 1) * size_page_favo), "\n")
            produit_substitue = self.manage.get_name_prod(
                i[0], self.cursor, self.connection
            )
            substitute = self.manage.get_name_prod(i[1], self.cursor, self.connection)
            print(
                produit_substitue[0][1],
                "       substitué par         ",
                substitute[0][1],
            )
            print("---------------------------")
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent  |  s : Page suivante  |  p : Page précédente\n-----------------------------------------------"
        )
        return ["menu6", favorites[1][0][0], list_favo_display]

    def menu7(self, favori_cursor, store_numbers):
        """This method manages the display of the menu for comparing a product to its substitute."""
        infos_prods_substituted = self.manage.get_all_infos_prod(
            favori_cursor["id_prod"], self.cursor, self.connection
        )
        infos_substitute = self.manage.get_all_infos_prod(
            favori_cursor["id_subs"], self.cursor, self.connection
        )
        print(
            "_______________________________________________\nMenu de détails du favori     \n_______________________________________________"
        )
        print("Produit substitué :")
        print("Nom :", infos_prods_substituted[0][0][1])
        print("Quantité :", infos_prods_substituted[0][0][2])
        print("Marque :", infos_prods_substituted[0][0][3])
        print("Catégories :", infos_prods_substituted[0][0][4])
        print("Labels :", infos_prods_substituted[0][0][5])
        print("Ingrédients :", infos_prods_substituted[0][0][6])
        allergens_display = ""
        for allerg in infos_prods_substituted[0][0][7][1:-1].split(","):
            if allerg[0] == " ":
                allerg = allerg[1:]
            allergens_display += allerg[4:-1] + ", "
        allergens_display = allergens_display[:-2]
        print("Allergènes :", allergens_display)
        traces_display = ""
        for trace in infos_prods_substituted[0][0][8][1:-1].split(","):
            if trace[0] == " ":
                trace = trace[1:]
            traces_display += trace[4:-1] + ", "
        traces_display = traces_display[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de traces :",
            traces_display,
        )
        print("Nutriscore :", infos_prods_substituted[0][0][9])
        print("Lien Open Foods Facts :", infos_prods_substituted[0][0][10])

        print("\nSubstitut :")
        print("Nom :", infos_substitute[0][0][1])
        print("Quantité :", infos_substitute[0][0][2])
        print("Marque :", infos_substitute[0][0][3])
        print("Catégories :", infos_substitute[0][0][4])
        print("Labels :", infos_substitute[0][0][5])
        print("Ingrédients :", infos_substitute[0][0][6])
        allergenes_display_infos_substitute = ""
        for allerg in infos_substitute[0][0][7][1:-1].split(","):
            if allerg[0] == " ":
                allerg = allerg[1:]
            allergenes_display_infos_substitute += allerg[4:-1] + ", "
        allergenes_display_infos_substitute = allergenes_display_infos_substitute[:-2]
        print("Allergènes :", allergenes_display_infos_substitute)
        traces_display_infos_substitute = ""
        for trace in infos_substitute[0][0][8][1:-1].split(","):
            if trace[0] == " ":
                trace = trace[1:]
            traces_display_infos_substitute += trace[4:-1] + ", "
        traces_display_infos_substitute = traces_display_infos_substitute[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de traces :",
            traces_display_infos_substitute,
        )
        print("Nutriscore :", infos_substitute[0][0][9])
        print("Lien Open Foods Facts :", infos_substitute[0][0][10])
        stores = self.manage.get_stores_prod(
            store_numbers, favori_cursor["id_subs"], self.cursor, self.connection
        )
        stor_display = ""
        for stor in stores[0]:
            stor_display += stor[0] + ", "
        stor_display = stor_display[:-2]
        print("Magasin  : ", stor_display)
        print(
            "-----------------------------------------------\nq : Quitter l'application  |  mp : Menu précédent\n-----------------------------------------------"
        )
        return "menu7"
