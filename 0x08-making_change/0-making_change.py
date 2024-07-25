#!/usr/bin/python3
"""
Change for the note
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    min_coins = [0] + [float("inf")] * total
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    return min_coins[-1] if min_coins[-1] != float("inf") else -1
