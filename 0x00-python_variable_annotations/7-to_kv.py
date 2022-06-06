#!/usr/bin/env python3
"""
type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
"""

from typing import Union


def to_kv(k: str, v: Union[int,float]) -> tuple:
    """Funtion that takes a strin and an int or float and returns a tuple"""
    new_tuple:tuple = (k, v)
    return new_tuple
