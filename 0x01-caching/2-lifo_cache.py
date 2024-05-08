#!/usr/bin/env python3
"""2. LIFO Caching"""
from base_caching import BaseCaching
from typing import Union


class LIFOCache(BaseCaching):
    """Defines LIFO replacement policy"""

    def put(self, key: str, item: str) -> None:
        """
        Assign to the dictionary `self.cache_data` the item `value` for the
        key `key`
        """
        if key and item:
            if len(
                    self.cache_data
            ) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                to_pop = list(self.cache_data.keys())[-1]
                self.cache_data.pop(to_pop)
                print("DISCARD:", to_pop)
            self.cache_data.update({key: item})

    # _____________________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
