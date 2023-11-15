import sqlite3

connection = sqlite3.connect("itstep10.sl3")
cur = connection.cursor()
#cur.execute("CREATE TABLE first_table(name TEXT);")
cur.execute("INSERT INTO first_table (name) VALUES ('Kira');")
cur.execute("INSERT INTO first_table (name) VALUES ('Arseniy');")
cur.execute("INSERT INTO first_table (name) VALUES ('Dmutro');")
cur.execute("INSERT INTO first_table (name) VALUES ('Artem');")
cur.execute("INSERT INTO first_table (name) VALUES ('Evgen');")
cur.execute("INSERT INTO first_table (name) VALUES ('Svatik');")
cur.execute("INSERT INTO first_table (name) VALUES ('Olekcandr');")
connection.commit()
connection.close()