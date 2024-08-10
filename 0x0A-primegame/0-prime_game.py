#!/usr/bin/python3
"""
0-prime_game.py
"""


def SOE(num):
    """Sieve of Eratosthenes
    get the first prime with all it's multiples
    then remove them from the round set

    Args:
        roundSeq (Set[integers]): set of round numbers
    returns:
        the rest of the set of round numbers
    """
    result = []
    muls = []
    prime = [True for i in range(num + 1)]
    p = 2
    seq = [i for i in range(1, num + 1)]
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False

        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            result.append(p)
            tmp = []
            for m in seq:
                if m in range(p, num + 1, p):
                    tmp.append(m)
            muls.append(tmp)

    return result, muls


def isWinner(x, nums):
    """Prime game
    on a x  rounds, get a number from nums,
    each participent, on a range of num,
    pick the first prime number, and all it's multiples from the range,
    until a participent at his turn, is found without any prime left to pick
    the other wins the round. thus by the x rounds ,
    the participent with max wins wins the game !

    Args:
        x (int): number of rounds
        nums (Set[int]): Set of numbers to interate on each round
    """
    if not x or not nums or x < 0 or nums == []:
        return None
    ben_wins = 0
    maria_wins = 0
    for i in range(x):
        if nums:
            num = nums.pop(0)
            if num <= 1:
                pass
            primes, multiples = SOE(num)
            turn = 'Maria'
            for i in range(num):
                if turn == 'Maria':
                    if primes:
                        primes.pop(0)
                        multiples.pop(0)
                        turn = 'Ben'
                    else:
                        ben_wins += 1
                        pass
                else:
                    if primes:
                        primes.pop(0)
                        multiples.pop(0)
                        turn = 'Maria'
                    else:
                        maria_wins += 1
        else:
            break

    if ben_wins > maria_wins:
        return 'Ben'
    elif maria_wins > ben_wins:
        return 'Maria'
    return None
