#!/usr/bin/env python3
"""class doc """

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """some doc"""
    if lst:
        return lst[0]
    else:
        return None
