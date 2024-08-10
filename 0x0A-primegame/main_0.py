#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(
    isWinner(5, [1000003, 1000033, 1000037, 1000039, 1000081])))
