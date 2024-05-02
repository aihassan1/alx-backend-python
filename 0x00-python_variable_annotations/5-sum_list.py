#!/usr/bin/env python3

"""
a type-annotated function sum_list which takes
a list input_list of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and return the sum"""
    sum = 0
    for item in input_list:
        sum = sum + item

    return sum
