"""This module allows the validation of products and the creation of data to be inserted into the database."""


class Validations:
    """This class is that of objects that sort products and create data to be inserted into the database.."""

    def __init__(self):
        """Init."""
        self.prods_stores = []
        self.prods_catego = []
        self.rows_prods = []
        self.rows_stores = []
        self.rows_cats = []
        self.rows_prods_cats = []
        self.rows_prods_stores = []

    def sort_build(self, obj_downlo):
        """This method makes it possible to sort the products and create the data to be inserted in the database."""
        # Construction of products
        list_prod = []
        for l_prod in obj_downlo.rows_prods:
            for prod0 in l_prod:
                try:
                    if (
                        (prod0["categories"] != "")
                        and (prod0["product_name"] != "")
                        and (prod0["nutriscore_data"]["grade"] != "")
                    ):
                        list_prod.append(prod0)
                except Exception as e:
                    pass
        self.rows_prods = list_prod

        # Construction of product-storeasins and products-categories dictionaries
        list_prod_store = []
        list_prod_catego = []
        for prod1 in self.rows_prods:
            try:
                list_store = prod1["stores"].split(",")
                try:
                    list_cat = prod1["categories"].split(",")
                    list_prod_store.append({prod1["code"]: list_store})
                    list_prod_catego.append({prod1["code"]: list_cat})
                except KeyError as e:
                    self.rows_prods.remove(prod1)
            except KeyError as e:
                self.rows_prods.remove(prod1)
        self.prods_stores = list_prod_store
        self.prods_catego = list_prod_catego

        # Construction of categories to insert
        for dict_prod_cat in self.prods_catego:
            for prod in dict_prod_cat:
                for cat in dict_prod_cat[prod]:
                    if cat[0] == " ":
                        cat = cat[1:]
                    if tuple([cat]) not in self.rows_cats:
                        self.rows_cats.append(tuple([cat]))

        # Construction of stores to insert
        for dict_prod_store in self.prods_stores:
            for store in dict_prod_store:
                for store in dict_prod_store[store]:
                    if store != "":
                        if store[0] == " ":
                            store = store[1:]
                    if tuple([store]) not in self.rows_stores:
                        self.rows_stores.append(tuple([store]))

        # Construction of category-product
        for prods in self.prods_catego:
            for key in prods:
                for cat in prods[key]:
                    if cat[0] == " ":
                        cat = cat[1:]
                    self.rows_prods_cats.append((key, cat))

        # Construction of products-stores
        for prods in self.prods_stores:
            for key in prods:
                for store in prods[key]:
                    if store != "":
                        if store[0] == " ":
                            store = store[1:]
                    self.rows_prods_stores.append((key, store))
