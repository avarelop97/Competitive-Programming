from collections import Counter

def first_non_repeating_letter(s: str) -> str:
    counts = Counter(c.casefold() for c in s)
    for c in s:
        if counts[c.casefold()] == 1:
            return c
    return ""