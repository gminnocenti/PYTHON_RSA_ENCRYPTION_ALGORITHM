import random

class LinearCongruentialGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        """Initialize the generator with seed, and optional parameters a, c, and m."""
        self.a = a
        self.c = c
        self.m = m
        self.state = seed

    def next(self):
        """Generate the next pseudorandom number."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

def is_prime(n, k=10):
    """Use the Miller-Rabin primality test to check if n is a probable prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find r and d such that n-1 = 2^r * d with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations of the test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_random_prime_in_range(lcg, min_value, max_value):
    """Generate a pseudorandom prime number within a specified range using LCG."""
    while True:
        # Generate a random candidate within the specified range
        candidate = lcg.next() % (max_value - min_value + 1) + min_value
        # Ensure the candidate is odd
        candidate |= 1
        if is_prime(candidate):
            return candidate

# Example usage
seed = random.randint(1,100000000)
lcg = LinearCongruentialGenerator(seed=seed)

# Generate a single pseudorandom prime number within the range [100, 1000]
min_value = 100
max_value = 1000
prime = generate_random_prime_in_range(lcg, min_value, max_value)
