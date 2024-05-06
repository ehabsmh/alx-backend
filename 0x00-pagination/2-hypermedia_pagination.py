#!/usr/bin/env python3
"""2. Hypermedia pagination"""
from typing import Tuple, List, Dict
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

    # _________________________________________________________________________________________

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    # _________________________________________________________________________________________

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

    # _________________________________________________________________________________________

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)

        page_dict = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page":  page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return page_dict
