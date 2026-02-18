def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product_3digits() -> tuple[int, int, int]:
    best = 0
    best_a = best_b = 0

    for a in range(999, 99, -1):
        # Poda por cota superior
        if a * 999 <= best:
            break

        # Si a no es múltiplo de 11, entonces b debe serlo (para palíndromos de 6 cifras)
        if a % 11 == 0:
            b_start, step = 999, 1
        else:
            b_start, step = 990, 11  # mayor múltiplo de 11 <= 999

        for b in range(b_start, a - 1, -step):  # b<=a evita duplicados
            prod = a * b

            # Poda interna
            if prod <= best:
                break

            if is_palindrome(prod):
                best = prod
                best_a, best_b = a, b
                break  # para este a, no habrá un b menor que mejore el prod

    return best, best_a, best_b

best, a, b = largest_palindrome_product_3digits()
print(best, a, b)  # 906609 993 913  (el orden puede variar)