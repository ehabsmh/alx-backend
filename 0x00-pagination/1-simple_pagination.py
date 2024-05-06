#!/usr/bin/env python3
"""1. Simple pagination"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters."""

    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page's dataset"""

        # Arguments should always be int
        assert type(page) is int and type(page_size) is int

        # Arguments page and page_size should be > 0
        assert page > 0 and page_size > 0

        try:
            # Get the specified index_range
            (start_index, end_index) = index_range(page, page_size)

            # Get the dataset
            dataset = self.dataset()

            # Return the dataset in the range of the specified indexes
            return dataset[start_index:end_index]
        except IndexError:
            return []
