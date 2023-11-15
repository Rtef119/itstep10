import sqlite3

connection = sqlite3.connect("itstep10.sl3")
cur = connection.cursor()

print(connection)
print(cur)
connection.close()