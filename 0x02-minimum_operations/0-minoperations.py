#!/usr/bin/python3
"""
This module defines a func for minOperations
"""


def minOperations(n):
    if n <= 1:
        return 0

    """Initialize an array to store the minimum operations
    needed for each position.
    """
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to have 1 H
    dp[1] = 0

    for i in range(2, n + 1):
        # Check if i is divisible by any number from 2 to sqrt(i)
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)

        # If i is a prime number
        if dp[i] == float('inf'):
            dp[i] = i

    return dp[n]
