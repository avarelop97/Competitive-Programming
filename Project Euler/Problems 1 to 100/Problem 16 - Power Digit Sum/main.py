def digit_sum_of_power(base: int, exp: int) -> int:
    n = pow(base, exp)          # exact big integer
    return sum(int(d) for d in str(n))

print(digit_sum_of_power(2, 1000))  # 1366