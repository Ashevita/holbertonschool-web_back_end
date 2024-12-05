#!/usr/bin/env python3
""" this module contains a function  sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers and floats and
    returns their sum as a float."""
    result: float = 0
    for i in mxd_lst:
        result += i
    return result
