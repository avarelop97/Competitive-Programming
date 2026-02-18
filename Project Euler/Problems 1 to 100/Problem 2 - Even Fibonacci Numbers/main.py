def sum_even_fib(limit: int = 4_000_000) -> int:
    # E1=2 (F2), E2=8 (F5)
    e_prev, e = 2, 8
    total = 2  # incluye E1

    while e <= limit:
        total += e
        e_prev, e = e, 4 * e + e_prev

    return total

print(sum_even_fib())  # 4613732