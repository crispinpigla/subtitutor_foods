"""This module manages the navigation of the application between different menus."""

from datetime import datetime

import mysql.connector

import config
import Console.display


class Navigation:
    """This class represents the class of the application object."""

    def __init__(self, display):
        """Init."""
        # Relative to display
        self.display = display

        # rows of elements in the database
        self.lines_cat_db = 0
        self.lines_prod_cat_db = 0
        self.lines_subst_prod_cat_db = 0
        self.lines_fav_db = 0

        # configurations
        self.page_catego = config.PAGE_CATEGORIES
        self.page_produ = config.PAGE_PRODUCTS
        self.page_subst = config.PAGE_SUBSTITUTES
        self.page_favo = config.PAGE_FAVORITES

        self.size_page_catego = config.SIZE_PAGE_CATEGORIES
        self.size_page_produ = config.SIZE_PAGE_PRODUITS
        self.size_page_subst = config.SIZE_PAGE_SUBSTITUTS
        self.size_page_favo = config.SIZE_PAGE_FAVORIS

        # the items displayed
        self.list_catego_display = []
        self.list_produ_display = []
        self.list_subst_display = []
        self.list_favo_display = []

        # the dotted elements
        self.category_cursor = {}
        self.product_cursor = {}
        self.substitut_cursor = {}
        self.favori_cursor = {}

    def distributor_menu(self):
        """This method manages the navigation of the application between different menus."""

        # Defining the selection status
        status = self.display.menu0()

        # Main loop
        while status != "off":

            # User input
            entr_util = input("\nEntrez une sélection : \n")

            # The application is in the main menu
            if status == "menu0":
                if entr_util == "1":
                    display_nav = self.display.menu1(
                        self.page_catego, self.size_page_catego
                    )
                    status = display_nav[0]
                    self.lines_cat_db = display_nav[1]
                    self.list_catego_display = display_nav[2]
                elif entr_util == "2":
                    display_nav = self.display.menu6(
                        self.size_page_favo, self.page_favo
                    )
                    status = display_nav[0]
                    self.lines_fav_db = display_nav[1]
                    self.list_favo_display = display_nav[2]
                elif entr_util == "q":
                    status = "off"
                else:
                    status = self.display.menu0()

            # The application is in the category menu
            elif status == "menu1":

                # selection next page
                if entr_util == "s":

                    # If the remainder of the division of the number of categories in the base by the size of the page is
                    # zero then the page number of categories is the division of the number of categories in the base by
                    # the size of the page. Otherwise the number of category pages is (the division of the number of
                    # categories in the base by the size of the page) + 1.
                    if (self.lines_cat_db % self.size_page_catego) == 0:
                        if self.page_catego < (
                            self.lines_cat_db // self.size_page_catego
                        ):
                            self.page_catego += 1
                        display_nav = self.display.menu1(
                            self.page_catego, self.size_page_catego
                        )
                        status = display_nav[0]
                        self.lines_cat_db = display_nav[1]
                        self.list_catego_display = display_nav[2]
                    elif (self.lines_cat_db % self.size_page_catego) > 0:
                        if self.page_catego < (
                            (self.lines_cat_db // self.size_page_catego) + 1
                        ):
                            self.page_catego += 1
                        display_nav = self.display.menu1(
                            self.page_catego, self.size_page_catego
                        )
                        status = display_nav[0]
                        self.lines_cat_db = display_nav[1]
                        self.list_catego_display = display_nav[2]

                # previous page selection
                elif entr_util == "p":
                    if self.page_catego > 1:
                        self.page_catego -= 1
                    display_nav = self.display.menu1(
                        self.page_catego, self.size_page_catego
                    )
                    status = display_nav[0]
                    self.lines_cat_db = display_nav[1]
                    self.list_catego_display = display_nav[2]

                # previous menu selection
                elif entr_util == "mp":
                    status = self.display.menu0()
                    self.page_catego = 1

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # selection of another choice
                else:

                    # select a category
                    try:

                        # The selected item is a number
                        page_ask = int(entr_util)
                        list_entr_flash = []
                        for cat in self.list_catego_display:
                            list_entr_flash.append(cat["selection"])

                        # The selected item is a number of the displayed selections
                        if page_ask in list_entr_flash:
                            for cat in self.list_catego_display:
                                if page_ask == cat["selection"]:
                                    self.category_cursor = cat
                            display_nav = self.display.menu2(
                                self.page_produ,
                                self.size_page_produ,
                                self.category_cursor,
                            )
                            status = display_nav[0]
                            self.lines_prod_cat_db = display_nav[1]
                            self.list_produ_display = display_nav[2]

                        # The selected item is a number of selections not displayed
                        else:
                            display_nav = self.display.menu1(
                                self.page_catego, self.size_page_catego
                            )
                            status = display_nav[0]
                            self.lines_cat_db = display_nav[1]
                            self.list_catego_display = display_nav[2]

                    # selection not listed
                    except:
                        display_nav = self.display.menu1(
                            self.page_catego, self.size_page_catego
                        )
                        status = display_nav[0]
                        self.lines_cat_db = display_nav[1]
                        self.list_catego_display = display_nav[2]

            # The application is in the products menu
            elif status == "menu2":

                # selection next page
                if entr_util == "s":
                    if (self.lines_prod_cat_db % self.size_page_produ) == 0:
                        if self.page_produ < (
                            self.lines_prod_cat_db // self.size_page_produ
                        ):
                            self.page_produ += 1
                        display_nav = self.display.menu2(
                            self.page_produ, self.size_page_produ, self.category_cursor
                        )
                        status = display_nav[0]
                        self.lines_prod_cat_db = display_nav[1]
                        self.list_produ_display = display_nav[2]
                    elif (self.lines_prod_cat_db % self.size_page_produ) > 0:
                        if self.page_produ < (
                            (self.lines_prod_cat_db // self.size_page_produ) + 1
                        ):
                            self.page_produ += 1
                        display_nav = self.display.menu2(
                            self.page_produ, self.size_page_produ, self.category_cursor
                        )
                        status = display_nav[0]
                        self.lines_prod_cat_db = display_nav[1]
                        self.list_produ_display = display_nav[2]

                # previous page selection
                elif entr_util == "p":
                    if self.page_produ > 1:
                        self.page_produ -= 1
                    display_nav = self.display.menu2(
                        self.page_produ, self.size_page_produ, self.category_cursor
                    )
                    status = display_nav[0]
                    self.lignes_prod_cat_bd = display_nav[1]
                    self.list_produ_display = display_nav[2]

                # previous menu selection
                elif entr_util == "mp":
                    display_nav = self.display.menu1(
                        self.page_catego, self.size_page_catego
                    )
                    status = display_nav[0]
                    self.lines_cat_db = display_nav[1]
                    self.list_catego_display = display_nav[2]
                    self.page_produ = 1

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # selection of another choice
                else:
                    try:
                        page_ask = int(entr_util)
                        list_entr_flash = []
                        for prod in self.list_produ_display:
                            list_entr_flash.append(prod["selection"])
                        if page_ask in list_entr_flash:
                            for prod in self.list_produ_display:
                                if page_ask == prod["selection"]:
                                    self.product_cursor = prod
                            display_nav = self.display.menu3(
                                self.category_cursor,
                                self.product_cursor,
                                self.size_page_subst,
                                self.page_subst,
                                config.STORES_NUMBER,
                            )
                            status = display_nav[0]
                            self.lines_subst_prod_cat_db = display_nav[1]
                            self.list_subst_display = display_nav[2]
                        else:
                            display_nav = self.display.menu2(
                                self.page_produ,
                                self.size_page_produ,
                                self.category_cursor,
                            )
                            status = display_nav[0]
                            self.lines_prod_cat_db = display_nav[1]
                            self.list_produ_display = display_nav[2]
                    except:
                        display_nav = self.display.menu2(
                            self.page_produ, self.size_page_produ, self.category_cursor
                        )
                        status = display_nav[0]
                        self.lines_prod_cat_db = display_nav[1]
                        self.list_produ_display = display_nav[2]

            # The application is in the substitutes menu
            elif status == "menu3":

                # selection next page
                if entr_util == "s":
                    if (self.lines_subst_prod_cat_db % self.size_page_subst) == 0:
                        if self.page_subst < (
                            self.lines_subst_prod_cat_db // self.size_page_subst
                        ):
                            self.page_subst += 1
                        display_nav = self.display.menu3(
                            self.category_cursor,
                            self.product_cursor,
                            self.size_page_subst,
                            self.page_subst,
                            config.STORES_NUMBER,
                        )
                        status = display_nav[0]
                        self.lines_subst_prod_cat_db = display_nav[1]
                        self.list_subst_display = display_nav[2]
                    elif (self.lines_subst_prod_cat_db % self.size_page_subst) > 0:
                        if self.page_subst < (
                            (self.lines_subst_prod_cat_db // self.size_page_subst) + 1
                        ):
                            self.page_subst += 1
                        display_nav = self.display.menu3(
                            self.category_cursor,
                            self.product_cursor,
                            self.size_page_subst,
                            self.page_subst,
                            config.STORES_NUMBER,
                        )
                        status = display_nav[0]
                        self.lines_subst_prod_cat_db = display_nav[1]
                        self.list_subst_display = display_nav[2]

                # previous page selection
                elif entr_util == "p":
                    if self.page_subst > 1:
                        self.page_subst -= 1
                    display_nav = self.display.menu3(
                        self.category_cursor,
                        self.product_cursor,
                        self.size_page_subst,
                        self.page_subst,
                        config.STORES_NUMBER,
                    )
                    status = display_nav[0]
                    self.lines_subst_prod_cat_db = display_nav[1]
                    self.list_subst_display = display_nav[2]

                # previous menu selection
                elif entr_util == "mp":
                    display_nav = self.display.menu2(
                        self.page_produ, self.size_page_produ, self.category_cursor
                    )
                    status = display_nav[0]
                    self.lines_prod_cat_db = display_nav[1]
                    self.list_produ_display = display_nav[2]
                    self.page_subst = 1

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # select a category
                else:

                    # select a category
                    try:
                        page_ask = int(entr_util)

                        list_entr_flash = []
                        for subs in self.list_subst_display:
                            list_entr_flash.append(subs["selection"])

                        if page_ask in list_entr_flash:
                            for subs in self.list_subst_display:
                                if page_ask == subs["selection"]:
                                    self.substitut_cursor = subs
                            display_nav = self.display.menu4(
                                self.substitut_cursor, config.STORES_NUMBER
                            )
                            status = display_nav[0]
                        else:
                            display_nav = self.display.menu3(
                                self.category_cursor,
                                self.product_cursor,
                                self.size_page_subst,
                                self.page_subst,
                                config.STORES_NUMBER,
                            )
                            status = display_nav[0]
                            self.lines_subst_prod_cat_db = display_nav[1]
                            self.list_subst_display = display_nav[2]

                    except:
                        display_nav = self.display.menu3(
                            self.category_cursor,
                            self.product_cursor,
                            self.size_page_subst,
                            self.page_subst,
                            config.STORES_NUMBER,
                        )
                        status = display_nav[0]
                        self.lines_subst_prod_cat_db = display_nav[1]
                        self.list_subst_display = display_nav[2]

            # The application is in the comparison menu of the product and the selected substitute
            elif status == "menu4":

                # previous menu selection
                if entr_util == "mp":
                    display_nav = self.display.menu3(
                        self.category_cursor,
                        self.product_cursor,
                        self.size_page_subst,
                        self.page_subst,
                        config.STORES_NUMBER,
                    )
                    status = display_nav[0]
                    self.lines_subst_prod_cat_db = display_nav[1]
                    self.list_subst_display = display_nav[2]

                # record selection
                elif entr_util == "e":
                    status = self.display.menu5(
                        self.product_cursor, self.substitut_cursor
                    )

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # other sélection
                else:
                    display_nav = self.display.menu4(
                        self.substitut_cursor, config.STORES_NUMBER
                    )
                    status = display_nav[0]

            # The application is in the menu of the confirmation of recordings (or message already recorded)
            elif status == "menu5":

                # sélection du menu précédent
                if entr_util == "mp":
                    display_nav = self.display.menu4(
                        self.substitut_cursor, config.STORES_NUMBER
                    )
                    status = display_nav[0]

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # other sélection
                else:
                    status = self.display.menu5(
                        self.product_cursor, self.substitut_cursor
                    )

            # The application is in the favorites menu
            elif status == "menu6":

                # selection next page
                if entr_util == "s":
                    if (self.lines_fav_db % self.size_page_favo) == 0:
                        if self.page_favo < (self.lines_fav_db // self.size_page_favo):
                            self.page_favo += 1
                        display_nav = self.display.menu6(
                            self.size_page_favo, self.page_favo
                        )
                        status = display_nav[0]
                        self.lines_fav_db = display_nav[1]
                        self.list_favo_display = display_nav[2]
                    elif (self.lines_fav_db % self.size_page_favo) > 0:
                        if self.page_favo < (
                            (self.lines_fav_db // self.size_page_favo) + 1
                        ):
                            self.page_favo += 1
                        display_nav = self.display.menu6(
                            self.size_page_favo, self.page_favo
                        )
                        status = display_nav[0]
                        self.lines_fav_db = display_nav[1]
                        self.list_favo_display = display_nav[2]

                # previous page selection
                elif entr_util == "p":
                    if self.page_subst > 1:
                        self.page_subst -= 1
                    display_nav = self.display.menu6(
                        self.size_page_favo, self.page_favo
                    )
                    status = display_nav[0]
                    self.lines_fav_db = display_nav[1]
                    self.list_favo_display = display_nav[2]

                # select previuos menu
                elif entr_util == "mp":
                    self.page_favo = 1
                    status = self.display.menu0()

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # select a category
                else:
                    # select a category
                    try:
                        page_ask = int(entr_util)
                        list_entr_flash = []
                        for fav in self.list_favo_display:
                            list_entr_flash.append(fav["selection"])
                        if page_ask in list_entr_flash:
                            for fav in self.list_favo_display:
                                if page_ask == fav["selection"]:
                                    self.favori_cursor = fav
                                    print(self.favori_cursor)
                            status = self.display.menu7(
                                self.favori_cursor, config.STORES_NUMBER
                            )
                        else:
                            display_nav = self.display.menu6(
                                self.size_page_favo, self.page_favo
                            )
                            status = display_nav[0]
                            self.lines_fav_db = display_nav[1]
                            self.list_favo_display = display_nav[2]

                    except:
                        display_nav = self.display.menu6(
                            self.size_page_favo, self.page_favo
                        )
                        status = display_nav[0]
                        self.lines_fav_db = display_nav[1]
                        self.list_favo_display = display_nav[2]

            # The application is in the product comparison and registered substitute menu
            elif status == "menu7":

                # previous menu selection
                if entr_util == "mp":
                    display_nav = self.display.menu6(
                        self.size_page_favo, self.page_favo
                    )
                    status = display_nav[0]
                    self.lines_fav_db = display_nav[1]
                    self.list_favo_display = display_nav[2]

                # select exit application
                elif entr_util == "q":
                    status = "off"

                # other selection
                else:
                    status = self.display.menu7(
                        self.favori_cursor, config.STORES_NUMBER
                    )
