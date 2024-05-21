from generador_numeros import LinearCongruentialGenerator,generate_random_prime_in_range
import random

def generate_key():
    
    seed = random.randint(1,100000000)
    lcg = LinearCongruentialGenerator(seed=seed)

    # Generate a single pseudorandom prime number within the range [100, 1000]
    min_value_pq = 100000000000000000
    max_value_pq = 1000000000000000000000000000000

    p = generate_random_prime_in_range(lcg, min_value_pq, max_value_pq)
    print(p)
    p_bytes = p.to_bytes((p.bit_length() + 7) // 8, byteorder='big')# Generate a 256-bit key (32 bytes)
    with open("secret.key", "wb") as key_file:
        key_file.write(p_bytes)

generate_key()