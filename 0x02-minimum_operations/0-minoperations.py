#!/usr/bin/python3
"""
module that defines the functions minOperations and prime_factorization.
"""


def minOperations(n):
    """calculates the fewest number of operations needed to result in n """
    if type(n) is not int or n <= 0:
        return 0
    return sum(prime_factorization(n))


def prime_factorization(n):
    """function that finds the prime factorization of a number"""
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors
