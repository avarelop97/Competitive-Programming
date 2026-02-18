def digit_sum(n: int) -> int:
    s = 0
    while n:
        n, r = divmod(n, 10)
        s += r
    return s

print(digit_sum(2**1000))  # 1366