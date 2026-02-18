import math

def digit_sum(x: int) -> int:
    s = 0
    while x:
        x, r = divmod(x, 10)
        s += r
    return s

def solve() -> int:
    return digit_sum(math.factorial(100))

if __name__ == "__main__":
    print(solve())  # 648