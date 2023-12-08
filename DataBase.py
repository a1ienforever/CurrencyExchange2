import sqlite3

import datetime

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS conversion (
        datetime DATETIME,
        rub INT,
        usd INT,
        crypt INT
        )""")

    db.commit()
    datetime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    rub = 100
    usd = 10
    crypt = 0.1

    cursor.execute(f"SELECT datetime FROM conversion WHERE datetime = '{datetime}'")
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO conversion VALUES(?,?,?,?)", (datetime, rub, usd, crypt))
        print('Запись сделана!')
    else:
        print("Error!")



