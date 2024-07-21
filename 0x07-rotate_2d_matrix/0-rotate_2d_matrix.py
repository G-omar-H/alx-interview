#!/usr/bin/env python3
"""
0-rotate_2d_matrix.py
"""

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Do not return anything. The matrix must be edited in-place.


    Args:
        matrix (_type_): _description_
    """
    if matrix is None:
        return None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            temp = matrix[row][len(matrix[row]) - 1]
            matrix[row][len(matrix[row]) - 1] = matrix[row][col]
            temp2 = matrix[len(matrix) - 1][len(matrix[row]) -1 ]
            matrix[len(matrix) - 1][len(matrix[row]) -1 ] = temp
            temp3 = matrix[len(matrix) - 1][col]
            matrix[len(matrix) - 1][col] = temp2
            matrix[row][col] = temp3

    """
    [                               [[7, 4, 1],
                                    [8, 5, 2],
                                    [9, 6, 3]]
                                    
                                    [1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]                       
    ]                           

    temp = 1
    temp2 = 9 
    temp3 = 7
    """