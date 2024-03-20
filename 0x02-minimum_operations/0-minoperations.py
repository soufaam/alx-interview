#!/usr/bin/python3
"""_summary_
"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 1 or n == 0 or n < 0:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[i // j] + j)
    return dp[n] if dp[n] != float('inf') else 0
