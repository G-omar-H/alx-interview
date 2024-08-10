#!/usr/bin/python3
import random
isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(
    isWinner(100, [random.randint(1, 10**6) for _ in range(100)])))
