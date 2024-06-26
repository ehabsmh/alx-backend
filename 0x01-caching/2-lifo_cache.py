#!/usr/bin/env python3
"""2. LIFO Caching"""
from base_caching import BaseCaching
from typing import Union


class LIFOCache(BaseCaching):
    """Defines LIFO replacement policy"""

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        # If cache is full and it is new item,
        # get the last item inserted in cache_data and del it
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            last_item: str = list(self.cache_data.keys())[-1]
            self.cache_data.popitem()
            print("DISCARD:", last_item)

        # Track access order for LIFO
        if key in self.cache_data:
            # Get the index of the existing key
            exist_key_index: int = list(self.cache_data.keys()).index(key)

            # Get the key from cache_data and delete it
            exist_key: str = list(self.cache_data.keys())[exist_key_index]
            self.cache_data.pop(exist_key)

        self.cache_data[key] = item

    # _____________________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
