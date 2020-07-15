"""
Ce module permet la validtion des produits et la création des données à insérer dans la base de donnée
"""


class Validations:
    """ Cette classe est celle des objets qui trient les produits et créent des données à insérer dans la base de donnée """

    def __init__(self):

        self.prods_mags = []
        self.prods_catego = []
        self.colonnes_prods = []
        self.colonnes_mags = []
        self.colonnes_cats = []
        self.colonnes_prods_cats = []
        self.colonnes_prods_mags = []

    def tri_build(self, obj_telech):
        """ Cette méthode permet de trier les produits et créer les données à insérer dans la base de donnée """

        # Construction des produits
        list_prod = []
        for l_prod in obj_telech.colonnes_prods:
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
        self.colonnes_prods = list_prod

        # Construction des dictionnaires produits-magasins et produits-catégories
        list_prod_mag = []
        list_prod_catego = []
        for prod1 in self.colonnes_prods:
            try:
                list_mag = prod1["stores"].split(",")
                try:
                    list_cat = prod1["categories"].split(",")
                    list_prod_mag.append({prod1["code"]: list_mag})
                    list_prod_catego.append({prod1["code"]: list_cat})
                except KeyError as e:
                    self.colonnes_prods.remove(prod1)
            except KeyError as e:
                self.colonnes_prods.remove(prod1)
        self.prods_mags = list_prod_mag
        self.prods_catego = list_prod_catego

        # Construction des Catégorie à insérer
        for dict_prod_cat in self.prods_catego:
            for prod in dict_prod_cat:
                for cat in dict_prod_cat[prod]:
                    if cat[0] == " ":
                        cat = cat[1:]
                    if tuple([cat]) not in self.colonnes_cats:
                        self.colonnes_cats.append(tuple([cat]))

        # Construction des magasins à insérer
        for dict_prod_mag in self.prods_mags:
            for mag in dict_prod_mag:
                for mag in dict_prod_mag[mag]:
                    if mag != "":
                        if mag[0] == " ":
                            mag = mag[1:]
                    if tuple([mag]) not in self.colonnes_mags:
                        self.colonnes_mags.append(tuple([mag]))

        # Construction des produits categories
        for prods in self.prods_catego:
            for key in prods:
                for cat in prods[key]:
                    if cat[0] == " ":
                        cat = cat[1:]
                    self.colonnes_prods_cats.append((key, cat))

        # Construction des produits magasins
        for prods in self.prods_mags:
            for key in prods:
                for mag in prods[key]:
                    if mag != "":
                        if mag[0] == " ":
                            mag = mag[1:]
                    self.colonnes_prods_mags.append((key, mag))
