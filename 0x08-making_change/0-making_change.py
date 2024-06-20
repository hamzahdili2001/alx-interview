#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """
    Calculates the minimum number of
    coins needed to make up a given total.
    """

    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    num_coins = 0

    for coin in sorted_coins:
        while total >= coin:
            num_coins += 1
            total -= coin

    if total == 0:
        return num_coins

    return -1
