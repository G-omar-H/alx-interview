#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Do not return anything. The matrix must be edited in-place.


    Args:
        matrix (List[List[int]]): matrix to rotate
    """
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
