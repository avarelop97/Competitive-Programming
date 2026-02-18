import math

def lattice_paths(n: int) -> int:
    # paths through n×n grid = C(2n, n)
    return math.comb(2 * n, n)

print(lattice_paths(20))  # 137846528820