





CREATE DATABASE p5 CHARACTER SET 'utf8';

--		Script de création de la base de données



USE p5;





CREATE TABLE Categories (
    id VARCHAR(100) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    id_produits MEDIUMTEXT,
    PRIMARY KEY (id)
)
ENGINE=INNODB;



CREATE TABLE Produits (
    id VARCHAR(25) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    quantite VARCHAR(255),
    marque VARCHAR(255),
    nom_categories VARCHAR(255),
    labels VARCHAR(255),
    pays_ventes VARCHAR(255),
    ingredients VARCHAR(255),
    produits_provoqu_ allergies VARCHAR(255),
    traces_eventuelles VARCHAR(255),
    nova VARCHAR(255),
    nutriscore VARCHAR(255),
    infos_nutritions TEXT NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE Magasins (
    id VARCHAR(150) NOT NULL,
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





...

--		Insertion des données



...

--		Script de recheche des categories correspondant à la demande de l’utilisateur





...

--		Recherche des produits correspondant à la demande de l’utilisteur






...

--		Recherche des substitus d'un produit







...

--		Enregistrement d'une recherche








...

--		Recherche des favoris








...

--		Recherche des informations d'un favoris















