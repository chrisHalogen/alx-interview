#!/usr/bin/python3
""" Function to calculate the minimum number of coins required
to reach a given total amount"""


def makeChange(coins, total):
    """Takes a list of coin denominations and calculates
    the minimum number of coins needed to make the given total"""
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while total >= i:
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
