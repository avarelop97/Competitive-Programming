import math
from functools import lru_cache


# --- Primality (deterministic for < 2^64, plenty for this problem) ---
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p

    # Miller-Rabin
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # Deterministic bases for 64-bit integers
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


# --- Concatenation without strings: a||b = a*10^{digits(b)} + b ---
@lru_cache(maxsize=None)
def pow10_for(b: int) -> int:
    # returns 10^{digits(b)}
    p = 10
    while b >= p:
        p *= 10
    return p

def concat(a: int, b: int) -> int:
    return a * pow10_for(b) + b


# --- Compatibility cache: (p,q) -> bool ---
@lru_cache(maxsize=None)
def compatible(p: int, q: int) -> bool:
    return is_prime(concat(p, q)) and is_prime(concat(q, p))


# --- Generate primes up to limit (simple sieve) ---
def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def solve(target_size: int = 5, prime_limit: int = 10_000) -> tuple[int, list[int]]:
    # candidates: exclude 2 and 5 (proof above)
    primes = [p for p in primes_upto(prime_limit) if p not in (2, 5)]

    # Build adjacency lists
    adj = {p: [] for p in primes}
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            if compatible(p, q):
                adj[p].append(q)
                adj[q].append(p)
    for p in primes:
        adj[p].sort()

    best_sum = 10**18
    best_clique: list[int] | None = None

    def search(clique: list[int], candidates: list[int], sum_so_far: int) -> None:
        nonlocal best_sum, best_clique
        k = len(clique)

        if sum_so_far >= best_sum:
            return
        if k == target_size:
            best_sum = sum_so_far
            best_clique = clique[:]
            return
        if len(candidates) < target_size - k:
            return

        for idx, p in enumerate(candidates):
            new_sum = sum_so_far + p
            if new_sum >= best_sum:
                break  # candidates are sorted ascending

            # Next candidates must be neighbors of p AND come after p to avoid duplicates
            neigh = set(adj[p])
            next_candidates = [q for q in candidates[idx + 1:] if q in neigh]
            search(clique + [p], next_candidates, new_sum)

    search([], primes, 0)
    if best_clique is None:
        raise RuntimeError("No solution found — increase prime_limit.")
    return best_sum, best_clique


if __name__ == "__main__":
    s, clique = solve(5, 10_000)
    print(s)       # 26033
    print(clique)  # [13, 5197, 5701, 6733, 8389]