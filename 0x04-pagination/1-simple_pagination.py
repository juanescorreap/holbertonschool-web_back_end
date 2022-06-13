#!/usr/bin/env python3
"""
index_range function and Server class with dataset and get_page methods
"""
import math
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a tuple containing a start
    index and an end index
    """
    upper_limit = (page * page_size) - page_size
    lower_limit = page * page_size
    indexes_range = (upper_limit, lower_limit)
    return indexes_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        upper_limit, lower_limit = index_range(page, page_size)
        return self.dataset()[upper_limit:lower_limit]
