import math

def solve() -> int:
    n = math.factorial(100)
    return sum(int(d) for d in str(n))

if __name__ == "__main__":
    print(solve())  # 648