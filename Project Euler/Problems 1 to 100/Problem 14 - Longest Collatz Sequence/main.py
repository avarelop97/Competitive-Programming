import math

def euler9(total: int = 1000) -> int:
    # total = 2*k*m*(m+n)  =>  k*m*(m+n) = total/2
    half = total // 2

    for m in range(2, int(math.isqrt(half)) + 1):
        if half % m != 0:
            continue

        # half = m * t  -> t = k*(m+n)
        t = half // m

        # ahora buscamos n y k: t = k*(m+n)
        # equivale a que (m+n) divide t
        for n in range(1, m):
            if t % (m + n) != 0:
                continue
            k = t // (m + n)

            a = k * (m*m - n*n)
            b = k * (2*m*n)
            c = k * (m*m + n*n)

            if a > 0 and b > 0 and a + b + c == total and a*a + b*b == c*c:
                a, b = sorted((a, b))
                return a * b * c

    raise RuntimeError("No solution found")

print(euler9(1000))  # 31875000