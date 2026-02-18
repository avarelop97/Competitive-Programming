from math import gcd

def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b

def sieve_primes(n: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)
        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]

def format_10_sig(x: float) -> str:
    # 10 significant digits => 1 digit before dot + 9 after dot in scientific notation
    mant, exp = f"{x:.9e}".split("e")
    return f"{mant}e{int(exp)}"

def g(n: int) -> float:
    # extract[i] = list of primes p such that i is a prime power p^k (k>=1)
    extract = [[] for _ in range(n + 1)]
    for p in sieve_primes(n):
        pk = p
        while pk <= n:
            extract[pk].append(p)
            pk *= p

    # dp[used] is dict: reduced_lcm -> weight
    dp = [dict() for _ in range(n + 1)]
    dp[0][1] = 1.0

    # process cycle lengths from n down to 1
    for i in range(n, 0, -1):
        new = [dict() for _ in range(n + 1)]

        for used in range(n + 1):
            if not dp[used]:
                continue
            max_a = (n - used) // i  # max number of i-cycles

            for L0, w0 in dp[used].items():
                # a = 0 (no i-cycles)
                new[used][L0] = new[used].get(L0, 0.0) + w0
                if max_a == 0:
                    continue

                # a >= 1 : LCM updates once with i (extra i-cycles don't change LCM)
                L1 = lcm(L0, i)

                # coefficient for a i-cycles: 1 / (i^a * a!)
                # build iteratively
                coeff = w0 / i            # a=1
                u = used + i
                new[u][L1] = new[u].get(L1, 0.0) + coeff

                for a in range(2, max_a + 1):
                    coeff /= (a * i)
                    u += i
                    new[u][L1] = new[u].get(L1, 0.0) + coeff

        # “lock in” prime-power factors at i
        if extract[i]:
            compressed = [dict() for _ in range(n + 1)]
            for used in range(n + 1):
                if not new[used]:
                    continue
                out = compressed[used]
                for L, w in new[used].items():
                    Lr, wr = L, w
                    # for each p where i == p^k:
                    # if current reduced LCM is divisible by p^k, remove one p and pay p^2 into weight
                    for p in extract[i]:
                        if Lr % i == 0:
                            Lr //= p
                            wr *= (p * p)
                    out[Lr] = out.get(Lr, 0.0) + wr
            new = compressed

        dp = new

    # after all extractions, reduced_lcm should end at 1
    return dp[n].get(1, 0.0)

if __name__ == "__main__":
    ans = g(350)
    print(format_10_sig(ans))  # -> 4.993401567e22