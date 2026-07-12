import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.join(BASE_DIR, "database.db")

SCHEMA = os.path.join(BASE_DIR, "schema.sql")

def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn

def init_db():

    conn = get_db()

    with open(SCHEMA) as f:

        conn.executescript(f.read())

    conn.close()

    print("Banco de dados criado.")

if __name__ == "__main__":

    init_db()