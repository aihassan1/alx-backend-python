#!/usr/bin/env python3
"""some discription """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    takes a list of integers lst and a float multiplier
    returns a new list where each element of lst is multiplied by multiplier
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
