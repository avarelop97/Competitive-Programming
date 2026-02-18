from __future__ import annotations

from math import prod
from pathlib import Path
from typing import Tuple


def greatest_adjacent_product(digits: str, k: int = 13) -> Tuple[int, str]:
    digits = "".join(digits.split())  # remove whitespace/newlines
    if not digits.isdigit():
        raise ValueError("Input contains non-digit characters after stripping whitespace.")
    if not (1 <= k <= len(digits)):
        raise ValueError("k must satisfy 1 <= k <= len(digits)")

    best = 0
    best_seq = ""

    window = [int(c) for c in digits[:k]]
    zero_count = sum(1 for x in window if x == 0)
    current = 0 if zero_count else prod(window)

    if current > best:
        best, best_seq = current, digits[:k]

    for i in range(k, len(digits)):
        out_d = window.pop(0)
        in_d = int(digits[i])
        window.append(in_d)

        if out_d == 0:
            zero_count -= 1
        if in_d == 0:
            zero_count += 1

        if zero_count:
            current = 0
        else:
            # safe rolling update when no zeros are involved; otherwise recompute once
            if out_d == 0:
                current = prod(window)
            else:
                current = (current // out_d) * in_d

        if current > best:
            best = current
            best_seq = digits[i - k + 1 : i + 1]

    return best, best_seq


def load_digits_from_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def solve(k: int = 13, matrix_path: Path | None = None) -> Tuple[int, str]:
    # Load ONLY during execution
    if matrix_path is None:
        matrix_path = Path(__file__).with_name("matrix.txt")

    digits = load_digits_from_txt(matrix_path)
    return greatest_adjacent_product(digits, k)


if __name__ == "__main__":
    best, seq = solve(13)
    print(best)  # 23514624000
    print(seq)   # 5576689664895