def sum_multiples(k: int, N: int) -> int:
    """
    Suma de los múltiplos positivos de k estrictamente menores que N.
    """
    m = (N - 1) // k
    return k * m * (m + 1) // 2

def euler1(N: int = 1000) -> int:
    return sum_multiples(3, N) + sum_multiples(5, N) - sum_multiples(15, N)

print(euler1(1000))  # 233168