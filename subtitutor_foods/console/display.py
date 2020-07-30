"""This module manages the display of the different menus."""

from subtitutor_foods.backend.manager import manager


class Display:
    """This class is the class of objects capable of generating displays.."""

    def __init__(self, cursor, connection):
        """Init."""
        # Relating to the connection to the database
        self.cursor = cursor
        self.connection = connection

        # the manager
        self.manage = manager.Managers()

    def main_menu(self):
        """This method controls the display of the main menu."""
        self.display_decoration("Menu principal", "_")
        print(
            "1\n\nRechercher des substitutes\n"
            + "-" * 27
            + "\n2\n\nConsulter les favorites\n"
            + "-" * 27
        )
        self.display_decoration("q : Quitter l'application", "-")
        return "main_menu"

    def category_menu(self, page_categories, size_page_categories):
        """This method manages the display of the category menu."""
        categories = self.manage.get_categories_size_page(
            size_page_categories, page_categories, self.cursor
        )
        self.display_decoration("Menu des catégories", "_")
        lines_categorie_database = categories[1][0][0]
        list_categories_display = []
        categories_display = {
            "selection": "", "id": "", "nom": "", "ids_prods": ""
        }
        for i in categories[0]:
            categories_display["selection"] = categories[0].index(i) + (
                    (page_categories - 1) * size_page_categories
            )
            categories_display["id"] = i[0]
            categories_display["nom"] = i[1]
            list_categories_display.append(categories_display)
            categories_display = {"selection": "", "nom": "", "ids_prods": ""}
            print(
                categories[0].index(i)
                + ((page_categories - 1) * size_page_categories),
                "--",
                i[1],
            )
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent   \ns : Page "
            "suivante  \np : Page précédente",
            "-",
        )
        return [
            "category_menu", lines_categorie_database, list_categories_display
        ]

    def products_menu(self, page_product, size_page_product, category_cursor):
        """This method manages the display of the products menu."""
        products = self.manage.get_products_size_page(
            category_cursor["nom"],
            size_page_product,
            page_product,
            self.cursor
        )
        lines_products_categories_database = products[1][0][0]
        list_product_display = []
        product_display = {"selection": "", "nutriscore": "", "id": ""}
        self.display_decoration("Menu des produits", "_")
        for i in products[0]:
            product_display["selection"] = products[0].index(i) + (
                    (page_product - 1) * size_page_product
            )
            product_display["nutriscore"] = i[4]
            product_display["id"] = i[0]
            list_product_display.append(product_display)
            product_display = {"selection": "", "nutriscore": "", "id": ""}
            print(
                products[0].index(i) + ((page_product - 1) * size_page_product)
            )
            print("Nom :", i[1])
            print("Quantité :", i[2])
            print("Marque :", i[3])
            print("Nutriscore :", i[4])
            print("---------------------------")
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent  \ns : Page "
            "suivante  \np : Page précédente",
            "-",
        )
        return [
            "products_menu",
            lines_products_categories_database, list_product_display
        ]

    def substitutes_menu(
            self,
            category_cursor,
            product_cursor,
            size_page_substitute,
            page_substitute,
            store_numbers,
    ):
        """This method manages the display of the substitutes menu."""
        substitutes = self.manage.get_substitutes_product(
            category_cursor["nom"],
            product_cursor["nutriscore"],
            size_page_substitute,
            page_substitute,
            self.cursor
        )
        lines_substitutes_product_categories_database = substitutes[1][0][0]
        self.display_decoration("Menu des substituts", "_")
        list_substitutes_display = []
        if lines_substitutes_product_categories_database == 0:
            print("\n" * 2, "Aucun résultat pour ce produit \n( Le nutriscore "
                            "du produit sélectionné est le plus faible "
                            "de sa categorie ) ", "\n" * 2)
        else:
            for i in substitutes[0]:
                stores = self.manage.get_stores_product(
                    store_numbers, i[0], self.cursor
                )
                list_substitutes_display.append(
                    {
                        "selection": substitutes[0].index(i) + 
                        ((page_substitute - 1)*size_page_substitute),
                        "id": i[0]
                     }
                )
                print(substitutes[0].index(i) + (
                        (page_substitute - 1) * size_page_substitute))
                print("Nom :", i[1])
                print("Quantité :", i[2])
                print("Marque :", i[3])
                print("Nutriscore :", i[4])
                store_display = ""
                for store in stores[0]:
                    store_display += store[0] + ", "
                store_display = store_display[:-2]
                print("Magasin  : ", store_display)
                print("---------------------------")
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent  \ns : Page "
            "suivante  \np : Page précédente",
            "-"
        )

        return ["substitutes_menu",
                lines_substitutes_product_categories_database,
                list_substitutes_display]

    def substitute_menu(self, substitute_cursor, store_numbers):
        """This method manages the display of the substitute menu."""
        products = self.manage.get_all_information_product(
            substitute_cursor["id"], self.cursor
        )
        self.display_decoration("Détails du substitut", "_")
        print("Nom :", products[0][0][1])
        print("Quantité :", products[0][0][2])
        print("Marque :", products[0][0][3])
        print("Catégories :", products[0][0][4])
        print("Labels :", products[0][0][5])
        print("Ingrédients :", products[0][0][6])
        allergens_display = ""
        for allergene in products[0][0][7][1:-1].split(","):
            if len(allergene) >= 1:
                if allergene[0] == " ":
                    allergene = allergene[1:]
                allergens_display += allergene[4:-1] + ", "
        allergens_display = allergens_display[:-2]
        print("Allergènes :", allergens_display)
        traces_display = ""
        for trace in products[0][0][8][1:-1].split(","):
            if len(trace) >= 1:
                if trace[0] == " ":
                    trace = trace[1:]
                traces_display += trace[4:-1] + ", "
        traces_display = traces_display[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de "
            "traces :",
            traces_display,
        )
        print("Nutriscore :", products[0][0][9])
        print("Lien Open Foods Facts :", products[0][0][10])
        stores = self.manage.get_stores_product(
            store_numbers, substitute_cursor["id"], self.cursor
        )
        store_display = ""
        for store in stores[0]:
            store_display += store[0] + ", "
        store_display = store_display[:-2]
        print("Magasin  : ", store_display)
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent  \ne : "
            "Enregistrer le substitut",
            "-",
        )
        return ["substitute_menu"]

    def registration_menu(self, product_cursor, substitute_cursor):
        """This method manages the display of the registration confirmation
        menu in the database. """
        check_favorite = self.manage.check_in_favorites(
            product_cursor["id"], substitute_cursor["id"], self.cursor
        )
        self.display_decoration("Menu d'enregistrement", "_")
        if check_favorite[0] == []:
            self.manage.add_in_favorites(
                product_cursor["id"],
                substitute_cursor["id"],
                self.cursor,
                self.connection,
            )
            print(
                "\n\n\n\n\nSubstitut enregistré dans vos favorites\n\n\n\n\n")
        else:
            print(
                "\n\n\n\n\nCet enregistrement est déjà dans vos "
                "favorites\n\n\n\n\n")
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent", "-"
        )
        return "registration_menu"

    def favorites_menu(self, size_page_favorite, page_favorite):
        """This method manages the display of the favorites menu."""
        favorites = self.manage.get_ids_favorites_size_page(
            size_page_favorite, page_favorite, self.cursor
        )
        self.display_decoration("Menu des favoris", "_")
        list_favorites_display = []
        for i in favorites[0]:
            list_favorites_display.append(
                {
                    "selection": favorites[0].index(i)
                    + (page_favorite - 1) * size_page_favorite,
                    "id_prod": i[0],
                    "id_subs": i[1],
                }
            )
            print(favorites[0].index(i) + (
                    (page_favorite - 1) * size_page_favorite), "\n")
            produit_substitue = self.manage.get_name_product(
                i[0], self.cursor
            )
            substitute = self.manage.get_name_product(i[1], self.cursor)
            print(
                produit_substitue[0][1],
                "       substitué par         ",
                substitute[0][1],
            )
            print('\nDate d\'enregistrement : ', i[2], '\n')
            print("---------------------------")
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent  \ns : Page "
            "suivante  \np : Page précédente",
            "-",
        )
        return ["favorites_menu", favorites[1][0][0], list_favorites_display]

    def comparing_product_substitute(self, favori_cursor, store_numbers):
        """This method manages the display of the menu for comparing a
        product to its substitute. """
        infos_products_substituted = self.manage.get_all_information_product(
            favori_cursor["id_prod"], self.cursor
        )
        infos_substitute = self.manage.get_all_information_product(
            favori_cursor["id_subs"], self.cursor
        )
        self.display_decoration("Menu de détails du favori", "_")
        print("Produit substitué :")
        print("Nom :", infos_products_substituted[0][0][1])
        print("Quantité :", infos_products_substituted[0][0][2])
        print("Marque :", infos_products_substituted[0][0][3])
        print("Catégories :", infos_products_substituted[0][0][4])
        print("Labels :", infos_products_substituted[0][0][5])
        print("Ingrédients :", infos_products_substituted[0][0][6])
        allergens_display = ""
        for allergene in infos_products_substituted[0][0][7][1:-1].split(","):
            if len(allergene) >= 1:
                if allergene[0] == " ":
                    allergene = allergene[1:]
                allergens_display += allergene[4:-1] + ", "
        allergens_display = allergens_display[:-2]
        print("Allergènes :", allergens_display)
        traces_display = ""
        for trace in infos_products_substituted[0][0][8][1:-1].split(","):
            if len(trace) >= 1:
                if trace[0] == " ":
                    trace = trace[1:]
                traces_display += trace[4:-1] + ", "
        traces_display = traces_display[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de "
            "traces :",
            traces_display,
        )
        print("Nutriscore :", infos_products_substituted[0][0][9])
        print("Lien Open Foods Facts :", infos_products_substituted[0][0][10])

        print("\nSubstitut :")
        print("Nom :", infos_substitute[0][0][1])
        print("Quantité :", infos_substitute[0][0][2])
        print("Marque :", infos_substitute[0][0][3])
        print("Catégories :", infos_substitute[0][0][4])
        print("Labels :", infos_substitute[0][0][5])
        print("Ingrédients :", infos_substitute[0][0][6])
        allergenes_display_infos_substitute = ""
        for allergene in infos_substitute[0][0][7][1:-1].split(","):
            if len(allergene) >= 1:
                if allergene[0] == " ":
                    allergene = allergene[1:]
                allergenes_display_infos_substitute += allergene[4:-1] + ", "
        allergenes_display_infos_substitute = allergenes_display_infos_substitute[
                                              :-2]
        print("Allergènes :", allergenes_display_infos_substitute)
        traces_display_infos_substitute = ""
        for trace in infos_substitute[0][0][8][1:-1].split(","):
            if len(trace) >= 1:
                if trace[0] == " ":
                    trace = trace[1:]
                traces_display_infos_substitute += trace[4:-1] + ", "
        traces_display_infos_substitute = traces_display_infos_substitute[:-2]
        print(
            "Substances susceptibles de provoquer des allergies à l'état de "
            "traces :",
            traces_display_infos_substitute,
        )
        print("Nutriscore :", infos_substitute[0][0][9])
        print("Lien Open Foods Facts :", infos_substitute[0][0][10])
        stores = self.manage.get_stores_product(
            store_numbers, favori_cursor["id_subs"], self.cursor
        )
        store_display = ""
        for store in stores[0]:
            store_display += store[0] + ", "
        store_display = store_display[:-2]
        print("Magasin  : ", store_display)
        self.display_decoration(
            "q : Quitter l'application  \nmp: Menu précédent", "-"
        )
        return ["comparing_product_substitute"]

    def display_decoration(self, title, decoration):
        """Display header and footer of menus."""
        if decoration == "_":
            print(
                "\n" * 5 + decoration * 50 + "\n"
                + title + "\n" + decoration * 50)
        else:
            print(decoration * 50 + "\n" + title + "\n" + decoration * 50)
