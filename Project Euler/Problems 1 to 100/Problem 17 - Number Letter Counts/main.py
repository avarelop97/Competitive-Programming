ONES = {
    0: 0,
    1: 3,   # one
    2: 3,   # two
    3: 5,   # three
    4: 4,   # four
    5: 4,   # five
    6: 3,   # six
    7: 5,   # seven
    8: 5,   # eight
    9: 4,   # nine
    10: 3,  # ten
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
}

TENS = {
    20: 6,  # twenty
    30: 6,  # thirty
    40: 5,  # forty
    50: 5,  # fifty
    60: 5,  # sixty
    70: 7,  # seventy
    80: 6,  # eighty
    90: 6,  # ninety
}

HUNDRED = 7   # "hundred"
AND = 3       # "and"
THOUSAND = 8  # "thousand"


def letters(n: int) -> int:
    if 0 <= n <= 19:
        return ONES[n]

    if 20 <= n <= 99:
        tens = (n // 10) * 10
        return TENS[tens] + ONES[n % 10]

    if 100 <= n <= 999:
        h = n // 100
        r = n % 100
        base = ONES[h] + HUNDRED
        if r == 0:
            return base
        return base + AND + letters(r)

    if n == 1000:
        return ONES[1] + THOUSAND

    raise ValueError("n out of supported range (0..1000)")


print(sum(letters(i) for i in range(1, 1001)))  # 21124