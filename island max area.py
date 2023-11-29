# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 12:58:33 2023

@author: Yang Cairong
"""

def max_island_area(grid):   
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0
        grid[row][col] = 0  # Mark the cell as visited (0) to avoid counting it again
        area = 1  # Current cell is part of the island
        for dr, dc in directions:
            area += dfs(row + dr, col + dc)
        return area

    if not grid:
        return 0


    max_area = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                max_area = max(max_area, dfs(row, col))

    return max_area

def flip_and_find_max_area(grid, row, col):
    # if not grid or 
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0

    # Flip the cell value (0 to 1 or 1 to 0)
    grid[row][col] = 1 - grid[row][col]

    # Recalculate the maximum island area after the flip
    max_area = max_island_area(grid)

    return max_area

# Example usage:
grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1]
]

print(max_island_area(grid))  # Output: 6

# Flip the cell at position (2, 1) from 0 to 1
print(flip_and_find_max_area(grid, 2, 1))  # Output: 8 (Maximum area after the flip)
