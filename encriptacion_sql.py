import sqlite3
from rsa import encriptar


mensaje='Criptografia'

mensaje_numero_lista_encriptado,q,e=encriptar(mensaje)
mensaje_numero_lista_encriptado_str = ",".join(mensaje_numero_lista_encriptado)

def agregar_sql(mensaje_numero_lista_encriptado_str,q,e):
    conn = sqlite3.connect('encriptacion.db')
    cursor = conn.cursor()

    # Insert data into the rsa table
    data=(mensaje_numero_lista_encriptado_str,q,e)
    cursor.execute('INSERT INTO rsa_new2 (mensaje, p, e) VALUES (?, ?, ?)', data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

agregar_sql(mensaje_numero_lista_encriptado_str,q,e)

print(mensaje_numero_lista_encriptado_str)