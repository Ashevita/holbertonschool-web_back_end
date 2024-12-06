#!/usr/bin/env python3
""" this module contains a function called sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list input_list of floats as argument and
    returns their sum as a float. """
    result: float = 0.0
    for i in input_list:
        result += i
    return result
