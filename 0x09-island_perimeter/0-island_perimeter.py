#!/usr/bin/python3
"""func definition"""


def island_perimeter(grid):
    if not grid:
        return 0
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume 4 edges around a land cell
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 for each shared edge btw adjacent land cells
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
