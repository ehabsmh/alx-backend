#!/usr/bin/env python3
"""4. MRU Caching"""
from base_caching import BaseCaching
from typing import Union
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Defines MRU replacement policy"""

    def __init__(self):
        super().__init__()
        self.ordered_cache_data = OrderedDict()
        self.cache_data = self.ordered_cache_data
        self.lru = []

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        if key not in self.ordered_cache_data:
            self.lru.append(key)

        # Existance items access should be updated
        if key in self.ordered_cache_data:
            self.lru.remove(key)
            self.lru.append(key)
            self.ordered_cache_data.move_to_end(key)

        # Delete least used item to insert a new item
        if (len(self.ordered_cache_data) == self.MAX_ITEMS
                and key not in self.ordered_cache_data):
            lru = self.lru[:-1].pop()
            del self.ordered_cache_data[lru]
            print("DISCARD:", lru)

        self.ordered_cache_data.update({key: item})

    # _____________________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        self.lru.remove(key)
        self.lru.append(key)

        return self.cache_data[key]
