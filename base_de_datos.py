import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)

# Create table rsa with columns mensaje, p, e
conn = sqlite3.connect('encriptacion.db')
cursor = conn.cursor()

# Create a new table with the desired column types
cursor.execute('''
CREATE TABLE rsa_new2 (
    mensaje VARCHAR(10000000),
    p BLOB,
    e BLOB
)
''')

conn.commit()
conn.close