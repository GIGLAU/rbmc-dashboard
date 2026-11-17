import sqlite3

conn = sqlite3.connect("rbmc.db")

print("Banco criado!")

conn.close()