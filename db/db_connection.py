"""cream conexiunea catre baza de date"""

import sqlite3

PATH_DB = "gestionare_stoc_produse.db"


def get_db_connection(db_path = PATH_DB):
    connection = sqlite3.connect(db_path)
    return connection


def create_database(db_path = PATH_DB):
    connection = sqlite3.connect(db_path)
    create_tables(connection)


def create_tables(connection):
    create_users_table(connection)
    create_products_table(connection)


def create_users_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
    id TEXT NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL);
    """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()


def create_products_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS products(
    id TEXT NOT NULL PRIMARY KEY,
    product_name TEXT NOT NULL,
    description TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    price REAL NOT NULL,
    weight INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0);
    """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()

