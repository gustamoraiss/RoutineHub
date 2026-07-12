import sqlite3

DATABASE = "database.db"

def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn

def init_db():

    conn = get_db()

    with open("schema.sql") as f:

        conn.executescript(f.read())

    conn.close()

    print("Banco de dados criado.")

