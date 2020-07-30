"""This module is responsible for creating the table and inserting
categories. """


class InstallationCategories:
    """
    This class is the class of objects responsible for creating 
    the table and inserting the categories.
    """

    def __init__(self):
        """Init."""
        pass

    def create_table_categories(self, cursor, connection):
        """This method allows the creation of the category table."""
        create_table_categories = (
            "CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT "
            "NULL AUTO_INCREMENT, "
            "nom VARCHAR(255) NOT NULL, PRIMARY KEY (id) ) ENGINE=INNODB "
        )
        cursor.execute(create_table_categories)
        connection.commit()

    def insert_rows_categories(self, validation, cursor, connection):
        """This method allows the insertion of categories."""
        add_categories = "INSERT INTO Categories (nom) VALUES (%s)"
        cursor.executemany(add_categories, validation.rows_categories)
        connection.commit()
        print("Insertion categories : ok")
