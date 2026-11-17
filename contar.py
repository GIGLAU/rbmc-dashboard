import sqlite3

conn = sqlite3.connect("rbmc.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM estacoes")

print(cursor.fetchone()[0])

conn.close()