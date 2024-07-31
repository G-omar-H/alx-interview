#!/usr/bin/env python3
"""
0x02. Minimum Operations
"""
from math import sqrt


def isprime(n) -> bool:
    """check if n is prime

    Args:
        n (int ): number to check

    Returns:
        bool: True if prime. False if not
    """
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def minOperations(n) -> int:
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n (int): number of characters

    Returns:
        int: number of operations
    """
    ans = 0
    if n <= 1:
        return 0
    elif isprime(n):
        return n
    for i in range(2, n)[::-1]:
        if isprime(i) and n % i == 0:
            ans += i
            ans += minOperations(int(n / i))
            break
    return ans
