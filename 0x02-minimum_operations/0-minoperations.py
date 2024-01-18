#!/usr/bin/python3
"""
get numb of operations
"""


def minOperations(n):
    """ min number of operation"""
    if not n and not isinstance(n, int) and n < 2:
        return 0

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i

    return operations
