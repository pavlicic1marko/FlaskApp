import sqlite3

conn = sqlite3.connect("cars.sqlite") # crete if not exist

cursor = conn.cursor()
sql_query = """CREATE TABLE cars  (id integer PRIMARY KEY,
        model text NOT NULL,
        price integer NOT NULL
)"""
cursor.execute(sql_query)