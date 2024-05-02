#!/usr/bin/env python3
"""element_length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A list of tuples, where each tuple contains an element
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
