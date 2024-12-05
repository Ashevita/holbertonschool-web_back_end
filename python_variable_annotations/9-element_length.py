#!/usr/bin/env python3
""" this module contains a function called sum_list """
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function lenght of an element """
    return [(i, len(i)) for i in lst]
