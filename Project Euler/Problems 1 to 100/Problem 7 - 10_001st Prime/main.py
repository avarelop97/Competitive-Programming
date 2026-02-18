import math

def nth_prime(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 2

    # Cota superior para p_n (válida para n>=6). Si n es pequeño, usamos un fallback.
    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    while True:
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[0:2] = b"\x00\x00"  # 0 y 1 no son primos

        # Criba
        r = int(math.isqrt(limit))
        for p in range(2, r + 1):
            if sieve[p]:
                start = p * p
                step = p
                sieve[start:limit + 1:step] = b"\x00" * (((limit - start) // step) + 1)

        # Contar hasta el n-ésimo primo
        count = 0
        for i, is_p in enumerate(sieve):
            if is_p:
                count += 1
                if count == n:
                    return i

        # Si el límite no fue suficiente, doblamos y repetimos (raro para este n).
        limit *= 2


print(nth_prime(10001))  # 104743