#!/usr/bin/python3
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
    memo = [sys.maxsize] * (total + 1)
    memo[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)

    return memo[total] if memo[total] != sys.maxsize else -1
