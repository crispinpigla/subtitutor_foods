import mysql.connector

import requests
import json


cnx = mysql.connector.connect(user="p5_user", password="motdepasse", database="p5_0")
cursor = cnx.cursor()
drop_table_0 = "DROP TABLE Favoris"
drop_table_1 = "DROP TABLE Categories"
drop_table_2 = "DROP TABLE Categories_produits"
drop_table_3 = "DROP TABLE Magasins"
drop_table_4 = "DROP TABLE Magasins_produits"
drop_table_5 = "DROP TABLE Produits"
cursor.execute(drop_table_0)
cursor.execute(drop_table_1)
cursor.execute(drop_table_2)
cursor.execute(drop_table_3)
cursor.execute(drop_table_4)
cursor.execute(drop_table_5)
cnx.commit()
cursor.close()
cnx.close()
