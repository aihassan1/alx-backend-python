#!/usr/bin/env python3
"""class doc """
from typing import Dict, Mapping, TypeVar, Union, Any

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from the dictionary
    Returns:
        The value associated with the key if it exists in the dictionary, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
