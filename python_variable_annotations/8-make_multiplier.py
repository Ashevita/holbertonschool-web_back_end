#!/usr/bin/env python3
""" this module contains a function called make_multiplier """
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier """
    def f(x: float) -> float:
        """ doing the math """
        return x * multiplier
    return f
