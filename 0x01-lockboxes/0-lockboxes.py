#!/usr/bin/env python3
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
    flag = True
    for i in range(len(boxes)):
        if i + 1 in boxes[i]:
          flag = True
        else:
            for j in boxes[i]:
                if j >= len(boxes):
                    pass
                elif i + 1 in boxes[j]:
                    flag = True
                else:
                    flag = False
    return flag

