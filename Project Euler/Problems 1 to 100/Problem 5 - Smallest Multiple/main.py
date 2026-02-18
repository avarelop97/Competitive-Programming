import math

def lcm_upto(n: int) -> int:
    x = 1
    for k in range(2, n + 1):
        x = x * k // math.gcd(x, k)
    return x

print(lcm_upto(20))  # 232792560