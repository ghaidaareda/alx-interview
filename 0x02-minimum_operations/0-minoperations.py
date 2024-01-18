#!/usr/bin/python3
"""
get numb of operations
"""


from sympy import factorint


def minOperations(n):
    """ min operation used"""
    if n < 2:
        return 0  # It's not possible to achieve n if n is less than 2

    factors = factorint(n)
    operations = sum(k * v for k, v in factors.items())
    return operations
