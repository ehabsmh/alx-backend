#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ if between two queries, certain rows are removed from the dataset,
        the user does not miss items from dataset when changing page."""
        assert (
            index is not None
            and index >= 0
            and index < len(self.__indexed_dataset)
        )

        data = []
        data_count = 0
        for indexed_key, item in self.__indexed_dataset.items():
            # Count of the appended data should be same to the page size
            if data_count == page_size:
                break

            # Define when should the appending start
            if indexed_key >= index:
                data.append(item)
                # Count the appended data
                data_count += 1

        return {
            "index": index,
            "next_index": indexed_key,
            "page_size": len(data),
            "data": data
        }
