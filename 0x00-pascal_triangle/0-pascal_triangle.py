#!/usr/bin/python

"""
Pascal triangle technical interview
"""


def pascal_triangle(n):
    """
    function that returns a list of a list of lists of integers
    representing the Pascal's triangle of n
    Args:
        n (int): number of rows
    """
    if n <= 0:
        return []
    rows = []
    for row in range(n):
        cols = []
        for col in range(row + 1):
            if col == 0:
                cols.append(1)
            elif col >= len(rows[row - 1]):
                cols.append(rows[row - 1][col - 1])
            else:
                cols.append(rows[row-1][col - 1] + rows[row - 1][col])
        rows.append(cols)
    return rows
