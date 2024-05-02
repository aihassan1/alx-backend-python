#!/usr/bin/env python3
"""some discription """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """doc for the function"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in

