def sum_proper_divisors_sieve(limit):
    # d[n] = sum of proper divisors of n, for 0 <= n < limit
    d = [0] * limit
    for i in range(1, limit // 2 + 1):
        for multiple in range(2 * i, limit, i):
            d[multiple] += i
    return d


def solve(limit=10000):
    d = sum_proper_divisors_sieve(limit)

    total = 0
    for a in range(2, limit):
        b = d[a]
        if b != a and b < limit and d[b] == a:
            total += a

    return total


if __name__ == "__main__":
    print(solve(10000))  # 31626