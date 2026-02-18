from __future__ import annotations

from pathlib import Path
from typing import List, Tuple


Grid = List[List[int]]


def load_grid_from_txt(path: Path) -> Grid:
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    grid: Grid = []
    for ln in lines:
        row = [int(x) for x in ln.split()]
        grid.append(row)

    # Basic sanity checks (optional but helpful)
    if not grid:
        raise ValueError("Empty grid file.")
    width = len(grid[0])
    if any(len(r) != width for r in grid):
        raise ValueError("Ragged grid: not all rows have the same length.")

    return grid


def greatest_product_in_grid(grid: Grid, k: int = 4) -> Tuple[int, Tuple[int, int], Tuple[int, int], List[int]]:
    """
    Returns:
      - best_product
      - start_cell (r, c)
      - direction (dr, dc)
      - the k values multiplied (for debugging / explanation)
    """
    rows, cols = len(grid), len(grid[0])

    # Canonical directions that cover all without duplication
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    best = -1
    best_start = (0, 0)
    best_dir = (0, 0)
    best_vals: List[int] = []

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                r_end = r + (k - 1) * dr
                c_end = c + (k - 1) * dc

                # Bounds check
                if not (0 <= r_end < rows and 0 <= c_end < cols):
                    continue

                prod = 1
                vals = []
                rr, cc = r, c
                for _ in range(k):
                    v = grid[rr][cc]
                    vals.append(v)
                    prod *= v
                    rr += dr
                    cc += dc

                if prod > best:
                    best = prod
                    best_start = (r, c)
                    best_dir = (dr, dc)
                    best_vals = vals

    return best, best_start, best_dir, best_vals


def solve(k: int = 4, grid_path: Path | None = None) -> int:
    # Load ONLY at runtime
    if grid_path is None:
        grid_path = Path(__file__).with_name("grid_20x20.txt")
    grid = load_grid_from_txt(grid_path)
    best, _, _, _ = greatest_product_in_grid(grid, k)
    return best


if __name__ == "__main__":
    ans = solve(4)
    print(ans)  # 70600674