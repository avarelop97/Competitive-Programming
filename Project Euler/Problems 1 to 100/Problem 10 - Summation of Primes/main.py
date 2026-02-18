import math

def sum_primes_below(n: int) -> int:
    if n <= 2:
        return 0

    # Representamos solo impares: 3,5,7,..., n-1
    size = (n - 3) // 2 + 1
    sieve = bytearray(b"\x01") * size  # 1 = "posible primo"

    r = int(math.isqrt(n - 1))         # solo necesitamos p <= sqrt(n-1)
    max_i = (r - 3) // 2               # índice máximo correspondiente a r

    for i in range(max_i + 1):
        if sieve[i]:
            p = 2 * i + 3
            start = (p * p - 3) // 2   # índice de p^2
            sieve[start::p] = b"\x00" * (((size - start - 1) // p) + 1)

    total = 2  # el primo 2
    for i, is_p in enumerate(sieve):
        if is_p:
            total += 2 * i + 3

    return total


print(sum_primes_below(2_000_000))  # 142913828922