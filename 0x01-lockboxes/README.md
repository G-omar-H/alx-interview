# 0x01. Lockboxes

### Project Overview

This project is part of the algorithmic training focused on the "Lockboxes" problem. The challenge is to determine if all boxes in a given set can be unlocked using the keys contained within the boxes.

**Project Duration:** Jun 3, 2024 4:00 AM - Jun 7, 2024 4:00 AM  
**Auto Review:** Will be launched at the deadline

### Table of Contents

- [Concepts Needed](#concepts-needed)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Lockboxes](#0-lockboxes)
- [Usage](#usage)
- [Author](#author)

### Concepts Needed

To successfully complete this project, you need a solid understanding of the following key concepts:

- **Lists and List Manipulation**
  - Understanding list operations such as accessing elements, iterating, and modifying lists.
  - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

- **Graph Theory Basics**
  - Basic knowledge of graph theory, especially traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS).
  - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms#graph-representation)

- **Algorithmic Complexity**
  - Understanding time and space complexity to write efficient algorithms.
  - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

- **Recursion**
  - Recursive approaches to problem-solving.
  - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

- **Queue and Stack**
  - Using queues and stacks for BFS or DFS.
  - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

- **Set Operations**
  - Using sets to keep track of visited boxes and available keys.
  - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Resources

- **Mock Technical Interview**

### Requirements

- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
  - All files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file at the root of the project directory is mandatory
  - Code should be documented
  - Code should use the PEP 8 style (version 1.7.x)
  - All files must be executable

### Tasks

#### 0. Lockboxes

**Score: 0.0% (Checks completed: 0.0%)**

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

**Prototype:** `def canUnlockAll(boxes)`  
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- Assume all keys will be positive integers (there can be keys that do not have boxes)
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

**Example:**

```python
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

Repository:

    GitHub repository: alx-interview
    Directory: 0x01-lockboxes
    File: 0-lockboxes.py


## Usage

To test the function, you can run the provided main_0.py file:

```sh

chmod +x main_0.py
./main_0.py
```

