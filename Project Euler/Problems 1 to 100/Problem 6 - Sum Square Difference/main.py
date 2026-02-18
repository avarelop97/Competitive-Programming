def sum_square_difference(n: int) -> int:
    s1 = n * (n + 1) // 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    return s1 * s1 - s2

print(sum_square_difference(100))  # 25164150