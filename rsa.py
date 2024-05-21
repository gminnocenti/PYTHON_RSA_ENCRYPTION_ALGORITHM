from generador_numeros import LinearCongruentialGenerator,generate_random_prime_in_range
from mapeoLetras_a_numeros import ascii_mapping,from_ascii_mapping
from leer_p import cargar_p
"""
- HACE FALTA CREAR BASE DE DATOS EN SQL CON COLUMNA MENSAJE_ENCRIPTADO | P | Q | E
- ALGORITMO DE ENCRIPTACION CON  .KEY LOCAL EL CUAL ENCRIPTA P Q E Y LO MANDA A LA BASE DE DATOS CON EL MENSAJE ENCRIPTADO MEDIANTE RSA
-ALGORITMO DE DESINCIPTACION QUE DESENCRIPTE P Q A 
"""
import random

def convertir_bytes(n):
    n_bytes = n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
    return n_bytes
def bytes_to_int(bytes_data):
    return int.from_bytes(bytes_data, byteorder='big')

def modulo(base,exponente,modulo):
    return pow(base, exponente, modulo)
def gcd(a, b):
    """Compute the greatest common divisor (GCD) of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a
def phi_n(p,q):
    phi=(p-1)*(q-1)
    return phi


############GENERAMOS P Y Q
def encriptar(mensaje_texto):
    seed = random.randint(1,100000000)
    lcg = LinearCongruentialGenerator(seed=seed)

    # Generate a single pseudorandom prime number within the range [100, 1000]
    min_value_pq = 100000000000000000
    max_value_pq = 1000000000000000000000000000000

    p=cargar_p()
    q= generate_random_prime_in_range(lcg, min_value_pq, max_value_pq)
    #asegurarme que p y que son diferentes
    while p == q:
        q = generate_random_prime_in_range(lcg, min_value_pq, max_value_pq)

    n=p*q
    ####GENERAR e

    min_value_e = 100
    phi_pq=phi_n(p,q)
    max_value_e= phi_n(p,q)-1
    e=generate_random_prime_in_range(lcg, min_value_e,max_value_e )
    while gcd(e,phi_pq)!=1:
        e=generate_random_prime_in_range(lcg, min_value_e,max_value_e )

    #CONVERTIR DE TEXTO A REPRESENTACION NUMERICA
    
    mensaje_numero_lista = ascii_mapping(mensaje_texto)
    #ENCRIPTAR
    mensaje_numero_lista_encriptado=[]
    for i in range(len(mensaje_numero_lista)):
        mensaje_numero=mensaje_numero_lista[i]
        encriptado=modulo(mensaje_numero,e,n)
        
        mensaje_numero_lista_encriptado.append(str(encriptado))
    print(mensaje_numero_lista_encriptado)
    print("q= ", q)
    print("e= ",e)
    return mensaje_numero_lista_encriptado,convertir_bytes(q),convertir_bytes(e)











#encontar d
def extended_gcd(a, b):
    """The extended Euclidean algorithm.
    Returns a tuple (g, x, y) such that a*x + b*y = g, where g is the gcd of a and b.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

def mod_inverse(a, m):
    """Find the multiplicative inverse of a modulo m using the Extended Euclidean Algorithm.
    Returns the inverse, or None if no inverse exists.
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        # No multiplicative inverse exists if gcd(a, m) != 1
        return None
    else:
        # x might be negative, so we take it modulo m to ensure it is positive
        return x % m
def modulo(base,exponente,modulo):
    return pow(base, exponente, modulo)
# Example usage
def desencriptar(mensaje_numero_lista_encriptado,q_bytes,e_bytes):
    q=bytes_to_int(q_bytes)
    e=bytes_to_int(e_bytes)
    p=cargar_p()
    n=p*q
    phi_pq=phi_n(p,q)
    d = mod_inverse(e, phi_pq)
    #####DESENCRIPTAR
    mensaje_numero_lista_desencriptado=[]
    for i in range(len(mensaje_numero_lista_encriptado)):
        c=mensaje_numero_lista_encriptado[i]
        decrypt=modulo(c,d,n)
        mensaje_numero_lista_desencriptado.append(decrypt)
    print(mensaje_numero_lista_desencriptado)
    mensaje_desencriptado=from_ascii_mapping(mensaje_numero_lista_desencriptado)
    print(mensaje_numero_lista_desencriptado)
    return mensaje_desencriptado

