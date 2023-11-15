import sqlite3

connection = sqlite3.connect("itstep_DB.sl3.")
cur = connection.cursor()
#cur.execute("CREATE TABLE first_table(name TEXT);")
'''cur.execute("INSERT INTO first_table(name) VALUES ('Kira');")
cur.execute("INSERT INTO first_table(name) VALUES ('Arsenij');")
cur.execute("INSERT INTO first_table(name) VALUES ('Evgen');")
cur.execute("INSERT INTO first_table(name) VALUES ('Timoxa');")
cur.execute("INSERT INTO first_table(name) VALUES ('Dmitro');")
cur.execute("INSERT INTO first_table(name) VALUES ('Artemij');")
cur.execute("INSERT INTO first_table(name) VALUES ('Svjatostav');")
cur.execute("INSERT INTO first_table(name) VALUES ('Olexandr');")'''
cur.execute("UPDATE first_table SET name='Evgenij' WHERE rowid=4")
connection.commit()
rez = cur.fetchall()
print(rez)

connection.commit()

connection.close()

