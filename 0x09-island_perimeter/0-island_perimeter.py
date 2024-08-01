#!/usr/bin/python3
from typing import List


def island_perimeter(grid: List[int]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:  # top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # right
                    perimeter += 1

    return perimeter
