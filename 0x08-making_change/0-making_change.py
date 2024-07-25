#!/usr/bin/env python3
"""
0-making_change.py
"""

import sys


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total

    Args:
        coins (List[int]): coins in possession
        total (int): total number to meet
    """
    if total <= 0:
        return 0
    seq = sys.maxsize
    flag = 0

    size = len(coins)

    for i in range(0, size):
        if coins[i] <= total:
            sub_seq = makeChange(coins, total - coins[i])
            if sub_seq != sys.maxsize and sub_seq + 1 < seq:
                seq = sub_seq + 1
    return seq
