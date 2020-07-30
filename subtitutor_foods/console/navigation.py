"""This module manages the navigation of the application between different
menus. """

from subtitutor_foods import config


class Navigation:
    """This class represents the class of the application object."""

    def __init__(self, display0):
        """Init."""
        # Relative to display
        self.display = display0

        # rows of elements in the database
        self.lines_categories_database = 0
        self.lines_products_categories_database = 0
        self.lines_subtitutes_products_categories_database = 0
        self.lines_favoris_database = 0

        # configurations
        self.page_categories = config.PAGE_CATEGORIES
        self.page_products = config.PAGE_PRODUCTS
        self.page_substitutes = config.PAGE_SUBSTITUTES
        self.page_favorites = config.PAGE_FAVORITES

        self.size_page_categories = config.SIZE_PAGE_CATEGORIES
        self.size_page_products = config.SIZE_PAGE_PRODUITS
        self.size_page_substitutes = config.SIZE_PAGE_SUBSTITUTS
        self.size_page_favorites = config.SIZE_PAGE_FAVORIS

        # the items displayed
        self.categories_display = []
        self.products_display = []
        self.substitutes_display = []
        self.favoris_display = []

        # the dotted elements
        self.category_cursor = {}
        self.product_cursor = {}
        self.substitut_cursor = {}
        self.favori_cursor = {}

    def distributor_menu(self):
        """This method manages the navigation of the application between
        different menus. """

        # Defining the selection status
        status = self.display.main_menu()

        # Main loop
        while status != "off":

            # User input
            user_input = input("\nEntrez une sélection : \n")

            # The application is in the main menu
            if status == "main_menu":
                status = self.ask_main_menu(user_input)

            # The application is in the category menu
            elif status == "category_menu":
                status = self.ask_category_menu(user_input)

            # The application is in the products menu
            elif status == "products_menu":
                status = self.ask_products_menu(user_input)

            # The application is in the substitutes menu
            elif status == "substitutes_menu":
                status = self.ask_substitutes_menu(user_input)

            # The application is in the comparison menu of the product and
            # the selected substitute
            elif status == "substitute_menu":
                status = self.ask_substitute_menu(user_input)

            # The application is in the menu of the confirmation of
            # recordings (or message already recorded)
            elif status == "registration_menu":
                status = self.ask_registration_menu(user_input)

            # The application is in the favorites menu
            elif status == "favorites_menu":

                status = self.ask_favorites_menu(user_input)

            # The application is in the product comparison and registered
            # substitute menu
            elif status == "comparing_product_substitute":
                status = self.ask_comparing_product_substitute(user_input)

    def ask_main_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        main menu. """
        if user_input == "1":
            status = self.get_display("category_menu", self.page_categories)
        elif user_input == "2":
            status = self.get_display("favorites_menu", self.page_favorites)
        elif user_input == "q":
            status = "off"
        else:
            status = self.display.main_menu()
        return status

    def ask_category_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        categories menu. """
        # selection next page
        if user_input == "s":
            status = self.manage_next_page("category_menu")

        # previous page selection
        elif user_input == "p":
            status = self.manage_previous_page("category_menu")

        # previous menu selection
        elif user_input == "mp":
            status = self.display.main_menu()
            self.page_categories = 1

        # select exit application
        elif user_input == "q":
            status = "off"

        # selection of another choice
        else:
            status = self.manage_selection(user_input, "category_menu")
        return status

    def ask_products_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        products menu. """
        # selection next page
        if user_input == "s":
            status = self.manage_next_page("products_menu")

        # previous page selection
        elif user_input == "p":
            status = self.manage_previous_page("products_menu")

        # previous menu selection
        elif user_input == "mp":
            status = self.get_display("category_menu", self.page_categories)
            self.page_products = 1

        # select exit application
        elif user_input == "q":
            status = "off"

        # selection of another choice
        else:
            status = self.manage_selection(user_input, "products_menu")

        return status

    def ask_substitutes_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        substitutes menu. """
        # selection next page
        if user_input == "s":
            status = self.manage_next_page("substitutes_menu")

        # previous page selection
        elif user_input == "p":
            status = self.manage_previous_page("substitutes_menu")

        # previous menu selection
        elif user_input == "mp":
            status = self.get_display("products_menu", self.page_products)
            self.page_substitutes = 1

        # select exit application
        elif user_input == "q":
            status = "off"

        # select a substitute
        else:
            status = self.manage_selection(user_input, "substitutes_menu")

        return status

    def ask_substitute_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        details substitute menu. """
        # previous menu selection
        if user_input == "mp":
            status = self.get_display("substitutes_menu",
                                      self.page_substitutes)

        # record selection
        elif user_input == "e":
            status = self.display.registration_menu(
                self.product_cursor, self.substitut_cursor
            )

        # select exit application
        elif user_input == "q":
            status = "off"

        # other sélection
        else:
            status = self.get_display("substitute_menu", None)

        return status

    def ask_registration_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        registration menu. """
        # sélection du menu précédent
        if user_input == "mp":
            status = self.get_display("substitute_menu", None)

        # select exit application
        elif user_input == "q":
            status = "off"

        # other sélection
        else:
            status = self.display.registration_menu(
                self.product_cursor, self.substitut_cursor
            )
        return status

    def ask_favorites_menu(self, user_input):
        """This method allows you to request a menu when the user is in the
        favorites menu. """
        # selection next page
        if user_input == "s":
            status = self.manage_next_page("favorites_menu")

        # previous page selection
        elif user_input == "p":
            status = self.manage_previous_page("favorites_menu")

        # select previuos menu
        elif user_input == "mp":
            self.page_favorites = 1
            status = self.display.main_menu()

        # select exit application
        elif user_input == "q":
            status = "off"

        # select a category
        else:
            status = self.manage_selection(user_input, "favorites_menu")

        return status

    def ask_comparing_product_substitute(self, user_input):
        """This method allows you to request a menu when the user is in the
        comparison menu of a product to his substitution. """
        # previous menu selection
        if user_input == "mp":
            status = self.get_display("favorites_menu", self.page_favorites)

        # select exit application
        elif user_input == "q":
            status = "off"

        # other selection
        else:
            status = self.get_display("comparing_product_substitute", None)

        return status

    def manage_next_page(self, which_menu):
        """This method is used to manage the selection of the next pages of
        the menus. """
        # If the remainder of the division of the number of categories in
        # the base by the size of the page is zero then the page number of
        # categories is the division of the number of categories in the base
        # by the size of the page. Otherwise the number of category pages is
        # (the division of the number of categories in the base by the size
        # of the page) + 1.
        page_menu = {
            "category_menu": self.page_categories,
            "products_menu": self.page_products,
            "substitutes_menu": self.page_substitutes,
            "favorites_menu": self.page_favorites,
        }
        lines_in_database = {
            "category_menu": self.lines_categories_database,
            "products_menu": self.lines_products_categories_database,
            "substitutes_menu": self.lines_subtitutes_products_categories_database,
            "favorites_menu": self.lines_favoris_database,
        }
        number_lines_display = {
            "category_menu": self.size_page_categories,
            "products_menu": self.size_page_products,
            "substitutes_menu": self.size_page_substitutes,
            "favorites_menu": self.size_page_favorites,
        }

        if (
                lines_in_database[which_menu] % number_lines_display[
                which_menu]
        ) == 0:
            if page_menu[which_menu] < (
                    lines_in_database[which_menu]
                    // number_lines_display[which_menu]
            ):
                if which_menu == "category_menu":
                    self.page_categories += 1
                    page = self.page_categories
                elif which_menu == "products_menu":
                    self.page_products += 1
                    page = self.page_products
                elif which_menu == "substitutes_menu":
                    self.page_substitutes += 1
                    page = self.page_substitutes
                elif which_menu == "favorites_menu":
                    self.page_favorites += 1
                    page = self.page_favorites
            else:
                page = page_menu[which_menu]
            status = self.get_display(which_menu, page)
        elif (
                lines_in_database[which_menu] % number_lines_display[
                which_menu]
        ) > 0:
            if page_menu[which_menu] < (
                    (
                            lines_in_database[which_menu]
                            // number_lines_display[which_menu]
                    )
                    + 1
            ):
                if which_menu == "category_menu":
                    self.page_categories += 1
                    page = self.page_categories
                elif which_menu == "products_menu":
                    self.page_products += 1
                    page = self.page_products
                elif which_menu == "substitutes_menu":
                    self.page_substitutes += 1
                    page = self.page_substitutes
                elif which_menu == "favorites_menu":
                    self.page_favorites += 1
                    page = self.page_favorites
            else:
                page = page_menu[which_menu]
            status = self.get_display(which_menu, page)
        return status

    def manage_previous_page(self, which_menu):
        """This method is used to manage the selection of the previous pages
        of the menus. """
        page_menu = {
            "category_menu": self.page_categories,
            "products_menu": self.page_products,
            "substitutes_menu": self.page_substitutes,
            "favorites_menu": self.page_favorites,
        }
        if page_menu[which_menu] > 1:
            if which_menu == "category_menu":
                self.page_categories -= 1
                page = self.page_categories
            elif which_menu == "products_menu":
                self.page_products -= 1
                page = self.page_products
            elif which_menu == "substitutes_menu":
                self.page_substitutes -= 1
                page = self.page_substitutes
            elif which_menu == "favorites_menu":
                self.page_favorites -= 1
                page = self.page_favorites
        else:
            page = page_menu[which_menu]
        status = self.get_display(which_menu, page)
        return status

    def get_display(self, which_menu, page):
        """allows to obtain a list of categories, products, substitutes or
        favorites according to the user's request. """
        if which_menu == "category_menu":
            display_navigation = self.display.category_menu(
                page, self.size_page_categories)
            status = display_navigation[0]
            self.lines_categories_database = display_navigation[1]
            self.categories_display = display_navigation[2]
            self.page_categories = page
        elif which_menu == "products_menu":
            display_navigation = self.display.products_menu(
                page, self.size_page_products, self.category_cursor
            )
            status = display_navigation[0]
            self.lines_products_categories_database = display_navigation[1]
            self.products_display = display_navigation[2]
            self.page_products = page
        elif which_menu == "substitutes_menu":
            display_navigation = self.display.substitutes_menu(
                self.category_cursor,
                self.product_cursor,
                self.size_page_substitutes,
                page,
                config.STORES_NUMBER,
            )
            status = display_navigation[0]
            self.lines_subtitutes_products_categories_database = display_navigation[1]
            self.substitutes_display = display_navigation[2]
            self.page_substitutes = page
        elif which_menu == "substitute_menu":
            display_navigation = self.display.substitute_menu(
                self.substitut_cursor, config.STORES_NUMBER
            )
            status = display_navigation[0]
        elif which_menu == "favorites_menu":
            display_navigation = self.display.favorites_menu(
                self.size_page_favorites, page)
            status = display_navigation[0]
            self.lines_favoris_database = display_navigation[1]
            self.favoris_display = display_navigation[2]
            self.page_favorites = page
        elif which_menu == "comparing_product_substitute":
            display_navigation = self.display.comparing_product_substitute(
                self.favori_cursor, config.STORES_NUMBER
            )
            status = display_navigation[0]
        else:
            status = "q"
        return status

    def manage_selection(self, user_input, which_menu):
        """This method is used to manage the selection of a category,
        product, substitute or favori. """
        next_menu = {
            "category_menu": "products_menu",
            "products_menu": "substitutes_menu",
            "substitutes_menu": "substitute_menu",
            "favorites_menu": "comparing_product_substitute",
        }
        page_next_menu = {
            "category_menu": self.page_products,
            "products_menu": self.page_substitutes,
            "substitutes_menu": None,
            "favorites_menu": None,
        }
        page_menu = {
            "category_menu": self.page_categories,
            "products_menu": self.page_products,
            "substitutes_menu": self.page_substitutes,
            "favorites_menu": self.page_favorites,
        }

        # Selection listed
        try:
            # The selected item is a number
            page_ask = int(user_input)
            entrance_flash = []
            if which_menu == "category_menu":
                displayed = self.categories_display
            elif which_menu == "products_menu":
                displayed = self.products_display
            elif which_menu == "substitutes_menu":
                displayed = self.substitutes_display
            elif which_menu == "favorites_menu":
                displayed = self.favoris_display
            for element_displayed in displayed:
                entrance_flash.append(element_displayed["selection"])

            # The selected item is a number of the displayed selections
            if page_ask in entrance_flash:
                for element_displayed in displayed:
                    if page_ask == element_displayed["selection"]:
                        if which_menu == "category_menu":
                            self.category_cursor = element_displayed
                        elif which_menu == "products_menu":
                            self.product_cursor = element_displayed
                        elif which_menu == "substitutes_menu":
                            self.substitut_cursor = element_displayed
                        elif which_menu == "favorites_menu":
                            self.favori_cursor = element_displayed

                status = self.get_display(
                    next_menu[which_menu], page_next_menu[which_menu]
                )

            # The selected item is a number of selections not displayed
            else:
                status = self.get_display(which_menu, page_menu[which_menu])

        # selection not listed
        except Exception as e:
            status = self.get_display(which_menu, page_menu[which_menu])
        return status