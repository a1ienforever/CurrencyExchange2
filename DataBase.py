import sqlite3

class DataBase:
    def start_database(self):
        with sqlite3.connect('identifier.sqlite') as db:
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS conversion(
            datetime DATETIME,
            rub INT,
            usd INT,
            crypt INT,
            name_crypt TEXT
            )""")
