import math

def num_divisors(x: int) -> int:
    """Return d(x) using prime factorization."""
    n = x
    total = 1

    # factor out 2
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    if e:
        total *= (e + 1)

    # odd factors
    p = 3
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            total *= (e + 1)
        p += 2

    # leftover prime
    if n > 1:
        total *= 2

    return total


def first_triangle_with_over_divisors(threshold: int = 500) -> int:
    n = 1
    while True:
        if n % 2 == 0:
            a = n // 2
            b = n + 1
        else:
            a = n
            b = (n + 1) // 2

        if num_divisors(a) * num_divisors(b) > threshold:
            return n * (n + 1) // 2

        n += 1


print(first_triangle_with_over_divisors(500))  # 76576500