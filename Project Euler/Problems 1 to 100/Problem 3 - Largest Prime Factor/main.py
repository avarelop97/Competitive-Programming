def largest_prime_factor(n: int) -> int:
    # 1) Quitar factor 2
    last = 1
    while n % 2 == 0:
        last = 2
        n //= 2

    # 2) Probar impares
    f = 3
    while f * f <= n:
        if n % f == 0:
            last = f
            n //= f
        else:
            f += 2

    # 3) Si queda n>1, es primo y es el mayor que queda
    return max(last, n)


N = 600_851_475_143
print(largest_prime_factor(N))  # 6857