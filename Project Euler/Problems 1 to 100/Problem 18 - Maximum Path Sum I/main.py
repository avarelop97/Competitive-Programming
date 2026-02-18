from pathlib import Path

DATA_FILE = "triangle.txt"


def load_triangle():
    path = Path(__file__).resolve().parent / DATA_FILE
    rows = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append([int(x) for x in line.split()])

    return rows


def max_path_sum(tri):
    # bottom-up DP (mutates tri)
    for r in range(len(tri) - 2, -1, -1):
        for c in range(len(tri[r])):
            tri[r][c] += max(tri[r + 1][c], tri[r + 1][c + 1])
    return tri[0][0]


if __name__ == "__main__":
    triangle = load_triangle()
    print(max_path_sum(triangle))  # 1074