# 0x02. Minimum Operations

**Curriculum Short Specializations Average: 74.33%**

## AlgorithmPython

### Project Overview

This project involves creating a method to calculate the minimum number of operations needed to result in exactly `n` characters in a file using only "Copy All" and "Paste" operations. This requires understanding and applying key algorithmic and mathematical concepts.

### Timeline

- **Project Start:** Jun 10, 2024, 4:00 AM
- **Project End:** Jun 14, 2024, 4:00 AM
- **Auto Review:** Launched at the deadline

### Key Concepts

1. **Dynamic Programming:**
   - Break down the problem into simpler subproblems and build up the solution.
   - [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

2. **Prime Factorization:**
   - Perform prime factorization as the problem can be reduced to finding the sum of the prime factors of the target number `n`.
   - [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:algebra-fundamentals/x2f8bb11595b61c86:prime-factorization/v/prime-factorization)

3. **Code Optimization:**
   - Approach problems from an optimization perspective to find the most efficient solution.
   - [How to optimize Python code](https://www.python.org/doc/essays/list2str/)

4. **Greedy Algorithms:**
   - Approach the problem with greedy algorithms, choosing the best option at each step.
   - [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

5. **Basic Python Programming:**
   - Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
   - [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

### Resources

- **Mock Technical Interview**

## Requirements

### General

- **Allowed editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS, Python 3.4.3
- **New Line:** All files should end with a new line.
- **Shebang:** The first line of all files should be `#!/usr/bin/python3`.
- **README:** A README.md file at the root of the project is mandatory.
- **Documentation:** Your code should be documented.
- **Style:** Code should use PEP 8 style (version 1.7.x).
- **Executable:** All files must be executable.

## Task

### 0. Minimum Operations

Create a method `def minOperations(n)` that calculates the fewest number of operations needed to result in exactly `n` characters in the file.

- **Prototype:** `def minOperations(n)`
- **Returns:** An integer
- **Edge Case:** If `n` is impossible to achieve, return 0

#### Example:

```python
n = 9
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

python

#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
##### Expected Output:

```bash

carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

## Repository

    GitHub repository: alx-interview
    Directory: 0x02-minimum_operations
    File: 0-minoperations.py

Copyright © 2024 ALX, All rights reserved
