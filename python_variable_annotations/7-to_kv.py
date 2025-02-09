#!/usr/bin/env python3
""" this module contains a function called  to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function to return a tuple """
    return (k, v ** 2)
