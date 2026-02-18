def lcm_upto_prime_powers(n: int) -> int:
    primes = []
    for x in range(2, n + 1):
        is_prime = True
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)

    result = 1
    for p in primes:
        power = p
        while power * p <= n:
            power *= p
        result *= power
    return result

print(lcm_upto_prime_powers(20))  # 232792560