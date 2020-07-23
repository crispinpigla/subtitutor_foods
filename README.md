# Application de recherche d'aliment
Application qui permet d'obtenir le substitut d'un produit à partir des données l'Open Foods Fact
# Installation
## installer mysql
Sous linux installer les client et serveur mysql grace à la commande `sudo apt-get install mysql-server mysql-client`
## Se connecter à mysql en mode root
Sous linux entrer la commande `sudo mysql`
## Creation de la base de données
Dans mysql entrer la commande `CREATE DATABASE database_name CHARACTER SET 'utf8';`
## Creation utilisateur
Dans mysql entrer la commande `CREATE USER 'p5_user'@'localhost' IDENTIFIED BY 'motdepasse';`
## Restreindre le privilèges de l'utilisateur de l'application
Dans mysql entrer la commande `GRANT ALL PRIVILEGES ON database_name.* TO 'p5_user'@'localhost';`
## Lancer l'application
Sous linux, dans l'invite commande, naviguer jusqu'au répertoire du fichier contenant l'application et executer la commande `python3 -m subtitutor_foods`
# Désinstaller l'application
Dans mysql entrer la commande `DROP DATABASE IF EXISTS database_name;`  
Entrer la commande la commande `DROP USER 'p5_user'@'localhost';`  
Ouvrir le fichier installation_status.json et changer la paramètre `installation_status` de `on` à `off`  
Supprimer le fichier contenant l'application