#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
     perimeter of the island described in grid:

    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn't have “lakes”
    (water inside that isn't connected to the water surrounding the island).


    Args:
        grid (List[List[int]]): list of lists of integers
            representing an Island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                if i == 0 or not grid[i - 1][j]:
                    perimeter += 1
                if j == 0 or not grid[i][j - 1]:
                    perimeter += 1
                if j == len(grid[i]) - 1 or not grid[i][j + 1]:
                    perimeter += 1
                if i == len(grid) - 1 or not grid[i + 1][j]:
                    perimeter += 1
    return perimeter
