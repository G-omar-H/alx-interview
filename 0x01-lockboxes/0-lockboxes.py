#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    check if boxes can be opened,
    only first box unlocked

    Args:
        boxes (List[List[int]]): n number of locked boxes
        Each box is numbered sequentially from 0 to n - 1
        and each box may contain keys to the other boxes.
    """
    open = 1
    visited = [0]
    keys_to_check = [0]
    while keys_to_check:
        i = keys_to_check.pop()
        for key in boxes[i]:
            if key in range(len(boxes)) and key not in visited:
                open += 1
                visited.append(key)
                keys_to_check.append(key)

    return open == len(boxes)
