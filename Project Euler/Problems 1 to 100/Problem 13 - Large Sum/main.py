from __future__ import annotations

from pathlib import Path


def first_digits_of_sum(path: Path, digits: int = 10) -> str:
    total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        total += int(line)
    return str(total)[:digits]


def solve(digits: int = 10, data_path: Path | None = None) -> str:
    # Load ONLY at runtime
    if data_path is None:
        data_path = Path(__file__).with_name("numbers.txt")
    return first_digits_of_sum(data_path, digits)


if __name__ == "__main__":
    print(solve(10))  # 5537376230