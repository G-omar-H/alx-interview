#!/usr/bin/python3
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

    triangle = [[1] * (row + 1) for row in range(n)]

    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1]\
                + triangle[row - 1][col]

    return triangle
