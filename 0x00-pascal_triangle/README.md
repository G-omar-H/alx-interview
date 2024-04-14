# Pascal's Triangle

## Table of Contents

- [About](#about)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Pascal's Triangle](#0-pascals-triangle)
- [Usage](#usage)
- [Repository](#repository)
- [License](#license)

## About
This project focuses on implementing Pascal's Triangle in Python. Pascal's Triangle is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal, in which each number is the sum of the two directly above it. This project serves as an opportunity to practice Python programming skills while exploring mathematical concepts.

## Resources
- [What is Pascal’s Triangle](#)
- [Pascal’s Triangle - Numberphile](#)
- [What are Python Algorithms](#)

## Requirements
To successfully complete this project, you should be familiar with the following Python concepts:
- **Lists and List Comprehensions**: Understand how to create, access, modify, and iterate over lists. Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.
- **Functions**: Know how to define and call functions. Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.
- **Loops**: Use for and while loops to iterate through sequences. Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.
- **Conditional Statements**: Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).
- **Recursion (Optional)**: While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle. Recognize base cases and recursive cases for a function that generates the triangle’s rows.
- **Arithmetic Operations**: Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.
- **Indexing and Slicing**: Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.
- **Memory Management**: Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.
- **Error and Exception Handling (Optional)**: Use try-except blocks as needed to handle potential errors, such as invalid input types or values.
- **Efficiency and Optimization**: Consider the time and space complexity of different approaches to generating Pascal’s Triangle. Evaluate and apply optimizations to improve the performance of the solution.

## Tasks
### 0. Pascal's Triangle
- **Mandatory**

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer

## Usage
To test the implementation of Pascal's Triangle, execute the provided test script:
```bash
./0-main.py
```

# Repository

    GitHub repository: alx-interview
    Directory: 0x00-pascal_triangle
    File: 0-pascal_triangle.py

# License

Copyright © 2024 ALX, All rights reserved.
