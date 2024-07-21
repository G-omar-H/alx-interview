# 0x07. Rotate 2D Matrix AlgorithmPython

## Overview
This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge tests your understanding of matrix manipulation and in-place operations in Python.

## Key Concepts

### Matrix Representation in Python
- **2D Matrices**: Represented using lists of lists.
- **Element Access and Modification**: Learn to access and modify elements in a 2D matrix.

### In-place Operations
- **Efficiency**: Perform operations without creating a copy of the data structure to minimize space complexity.

### Matrix Transposition
- **Definition**: Swapping rows and columns in a matrix.
- **Implementation**: Essential step in the rotation process.

### Reversing Rows in a Matrix
- **Row Manipulation**: Reverse the order of rows as part of the rotation.

### Nested Loops
- **Iteration**: Use nested loops to iterate through 2D data structures.
- **Element Modification**: Achieve the desired rotation through nested loops.

## Resources

- **Python Official Documentation**:
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  
- **GeeksforGeeks Articles**:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
  
- **TutorialsPoint**:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Approach

1. **Transpose the Matrix**: Swap rows with columns.
2. **Reverse Each Row**: Reverse the order of elements in each row to achieve the 90-degree clockwise rotation.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS with python3 (version 3.8.10)
- **Style Guide**: Follow the pycodestyle style (version 2.8.0)
- **Documentation**: Document all modules and functions
- **Execution**: Ensure all files are executable and end with a new line

## Task

### Rotate 2D Matrix

- **Objective**: Rotate an n x n 2D matrix by 90 degrees clockwise in-place.
- **Prototype**: `def rotate_2d_matrix(matrix):`
- **Constraints**: 
  - Do not return anything.
  - Assume the matrix is non-empty and has 2 dimensions.

**Example:**

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```
Expected Output:

```lua

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository

    GitHub repository: alx-interview
    Directory: 0x07-rotate_2d_matrix
    File: 0-rotate_2d_matrix.py
