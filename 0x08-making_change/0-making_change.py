#!/usr/bin/python3
"""Making changes"""


def makeChange(coins, total):
    """making change function """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
