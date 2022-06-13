#!/usr/bin/env python3
"""
Function named index_range that takes two integer
arguments page and page_size and returns a tuple
of size two containing a start index and an end
index corresponding to the range of indexes to
return in a list for those particular pagination
parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a tuple containing a start
    index and an end index
    """
    upper_limit = (page * page_size) - page_size
    lower_limit = page * page_size
    indexes_range = (upper_limit, lower_limit)
    return indexes_range
