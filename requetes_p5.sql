





CREATE DATABASE p5 CHARACTER SET 'utf8';

--		Script de création de la base de données



USE p5;

--		Sélection de la base




CREATE TABLE Categories (
    id VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    id_produits MEDIUMTEXT,
    PRIMARY KEY (id)
)
ENGINE=INNODB;



CREATE TABLE Produits (
    id VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    quantite VARCHAR(255),
    marque VARCHAR(255),
    nom_categories VARCHAR(255),
    labels VARCHAR(255),
    pays_ventes VARCHAR(255),
    ingredients VARCHAR(255),
    produits_provoqu_allergies VARCHAR(255),
    traces_eventuelles VARCHAR(255),
    nova VARCHAR(255),
    nutriscore VARCHAR(255),
    infos_nutritions TEXT NOT NULL,
    lien_o_ff VARCHAR(255),
    PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE Magasins (
    id VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    id_produits MEDIUMTEXT,
    PRIMARY KEY (id)

)
ENGINE=INNODB;


CREATE TABLE Favoris (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_produit VARCHAR(50) NOT NULL,
    id_resultats VARCHAR(255) NOT NULL,
    date_enregistrement DATETIME NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;



--		Création des tables





INSERT INTO Categories
VALUES ('chien', 'F', '2008-12-06 05:18:00', 'Caroline'),
        ('chat', 'M', '2008-09-11 15:38:00', 'Bagherra'),
        ('tortue', NULL, '2010-08-23 05:18:00', NULL);
...

--		Insertion des données



SELECT nom, id_produits 
FROM Categories
ORDER BY nom
LIMIT taille_page_cat OFFSET (numero_page - 1)*taille_page_cat ;

--		Script de recheche des categories correspondant à la demande de l’utilisateur





SELECT nom, quantite, marque, nutriscore
FROM Produits
WHERE id IN tableau_ids_produits
ORDER BY nom
LIMIT taille_page_prod OFFSET (numero_page - 1)*taille_page_prod ;

--		Recherche des produits correspondant à la demande de l’utilisteur






SELECT nom, quantite, marque, labels, ingredients, produits_provoqu_allergies, traces_eventuelles, nova, nutriscore, infos_nutritions
FROM Produits
WHERE nutriscore IN tableau_nutriscores_chercher
ORDER BY nutriscore
LIMIT nombre_substituts OFFSET 0 ;

--		Recherche des substitus d'un produit







INSERT INTO Favoris ( id_produit, id_resultats, date_enregistrement )
VALUES ( id_prod, id_results, NOW() )

--		Enregistrement d'une recherche








SELECT *
FROM Favoris
LIMIT taille_page_fav OFFSET (numero_page_fav - 1)*taille_page_fav ;

SELECT id, nom, quantite, marque, nutriscore
FROM Produits
WHERE id IN tableau_ids_produits

--		Recherche des favoris








SELECT id, nom, quantite, marque, labels, ingredients, produits_provoqu_allergies, traces_eventuelles, nova, nutriscore, infos_nutritions
FROM Produits
WHERE id IN tableau_ids_produits

--		Recherche des informations d'un favoris















