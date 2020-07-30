"""This module is used to create the application database."""

import mysql.connector

from subtitutor_foods import config


class CreateDataBase:
    """This class is the creation class of the application database."""

    def __init__(self):
        """Init."""
        pass

    def create_database(self, cursor, connection):
        """This method is used to create the application database."""
        create_database = ("CREATE DATABASE IF NOT EXISTS "
                           + config.DATABASES_NAME
                           + " CHARACTER SET 'utf8'")
        cursor.execute(create_database)
        connection.commit()
        return mysql.connector.connect(user=config.USER_NAME,
                                       password=config.PASSEWORD,
                                       database=config.DATABASES_NAME)
