#!/usr/bin/env python3
"""1. FIFO caching"""
from base_caching import BaseCaching
from typing import Union


class FIFOCache(BaseCaching):
    """Defines FIFO replacement policy"""

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first item was inserted in cache_data and delete it.
            first_item = list(self.cache_data.keys())[0]
            print("DISCARD:", first_item)
            self.cache_data.pop(first_item)

    # ______________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
