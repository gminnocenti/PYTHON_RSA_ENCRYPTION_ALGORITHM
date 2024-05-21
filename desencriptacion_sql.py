import sqlite3
from rsa import desencriptar
def get_last_row():
    # Connect to the database
    conn = sqlite3.connect('encriptacion.db')
    cursor = conn.cursor()

    # Query to get the last row
    cursor.execute('SELECT mensaje, p, e FROM rsa_new2 ORDER BY ROWID DESC LIMIT 1')
    last_row = cursor.fetchone()

    # Close the connection
    conn.close()

    return last_row

def desencriptar_mensaje():
    last_row = get_last_row()

    c=last_row[0]
    q=last_row[1]
    e=last_row[2]

    c_lista = c.split(",")
    c_int_list = [int(item) for item in c_lista]

    m=desencriptar(c_int_list,q,e)
    print(m)
desencriptar_mensaje()