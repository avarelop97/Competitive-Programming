from pathlib import Path

DATA_FILE = "names.txt"

def name_value(name: str) -> int:
    # name is uppercase A-Z
    return sum(ord(ch) - ord("A") + 1 for ch in name)

def solve() -> int:
    path = Path(__file__).resolve().parent / DATA_FILE
    raw = path.read_text(encoding="utf-8").strip()

    # File format: "MARY","PATRICIA","LINDA",...
    names = raw.replace('"', "").split(",")
    names.sort()

    total = 0
    for i, name in enumerate(names, start=1):  # 1-based position
        total += i * name_value(name)

    return total

if __name__ == "__main__":
    print(solve())  # 871198282