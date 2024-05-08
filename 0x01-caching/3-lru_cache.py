#!/usr/bin/env python3
"""3. LRU Caching"""
from base_caching import BaseCaching
from typing import Union
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Defines LRU replacement policy"""

    def __init__(self):
        super().__init__()
        self.ordered_cache_data = OrderedDict()
        self.cache_data = self.ordered_cache_data

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        # Existance items access should be updated
        if key in self.ordered_cache_data:
            self.ordered_cache_data.move_to_end(key)

        # Delete least used item to insert a new item
        if (len(self.ordered_cache_data) == self.MAX_ITEMS
                and key not in self.ordered_cache_data):
            least_used: str = list(self.ordered_cache_data.keys())[0]
            self.ordered_cache_data.pop(least_used)
            print("DISCARD:", least_used)

        self.ordered_cache_data.update({key: item})

    # _____________________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        self.ordered_cache_data.move_to_end(key)

        return self.cache_data[key]
