#!/usr/bin/python3
"""
Module: Prime Number Selection Game
"""


def primeNumbers(n):
    """
    Returns a list of prime numbers between 1 and n (inclusive).
    Args:
        n (int): The upper limit of the range (starting from 1).
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    Args:
        x (int): The number of rounds to be played.
        nums (int): The upper limit of the number range for each round.
    Returns:
        str: The name of the winner ('Maria' or 'Ben'), or None if no winner can be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
