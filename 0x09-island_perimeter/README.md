# 0x09. Island Perimeter

## AlgorithmPython

### Project Overview

This project involves creating a function to calculate the perimeter of an island in a 2D grid. You will apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve this geometric problem.

### Timeline

- **Project Start:** Jul 29, 2024, 4:00 AM
- **Project End:** Aug 2, 2024, 4:00 AM
- **Checker Release:** Jul 30, 2024, 4:00 AM
- **Auto Review Launch:** At the deadline

## Key Concepts

### 2D Arrays (Matrices)

- **Accessing and Iterating:** Navigate through elements in a 2D array.
- **Adjacent Cells:** Understand how to navigate through horizontally and vertically adjacent cells.

### Conditional Logic

- **Conditions:** Determine whether a cell contributes to the perimeter of the island.

### Counting Techniques

- **Edge Counting:** Develop a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies

- **Break Down:** Identify land cells and calculate their contribution to the perimeter.

### Python Programming

- **Nested Loops:** Iterate over grid cells.
- **Conditional Statements:** Check the status of adjacent cells.

## Resources

### Python Official Documentation

- [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-lists): Understanding how to work with lists within lists in Python.

### GeeksforGeeks Articles

- [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.

### TutorialsPoint

- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, essential for working with a grid.

### YouTube Tutorials

- [Python 2D arrays and lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists): Various tutorials explaining the concepts.

## Requirements

### General

- **Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS, Python 3.4.3
- **New Line:** All files should end with a new line.
- **Shebang:** The first line of all files should be `#!/usr/bin/python3`.
- **README:** A README.md file at the root of the project is mandatory.
- **Style:** Code should use PEP 8 style (version 1.7).
- **Modules:** No module imports allowed.
- **Documentation:** All modules and functions must be documented.
- **Executable:** All files must be executable.

## Task

### 0. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the grid:

- **Grid:** A list of lists of integers:
  - `0` represents water
  - `1` represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - Grid is rectangular, with its width and height not exceeding 100
- **Assumptions:**
  - The grid is completely surrounded by water.
  - There is only one island (or nothing).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
```

Expected Output:

```ruby

guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$
```

## Repository

    GitHub repository: alx-interview
    Directory: 0x09-island_perimeter
    File: 0-island_perimeter.py

Copyright © 2024 ALX, All rights reserved
