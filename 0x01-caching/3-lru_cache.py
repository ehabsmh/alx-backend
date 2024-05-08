#!/usr/bin/env python3
"""3. LRU Caching"""
from base_caching import BaseCaching
from typing import Union
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Defines LRU replacement policy"""

    def __init__(self):
        super().__init__()
        self.my_ordered_dict = OrderedDict()
        self.cache_data = self.my_ordered_dict

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        # Delete least used item to insert a new item
        if (len(self.my_ordered_dict) == self.MAX_ITEMS
                and key not in self.my_ordered_dict):
            least_used: str = list(self.my_ordered_dict.keys())[0]
            self.my_ordered_dict.pop(least_used)
            print("DISCARD:", least_used)

        # Existance items access should be updated
        elif (len(self.my_ordered_dict) == self.MAX_ITEMS
                and key in self.my_ordered_dict):
            self.my_ordered_dict.move_to_end(key)

        self.my_ordered_dict.update({key: item})

    # _____________________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        self.my_ordered_dict.move_to_end(key)

        return self.cache_data[key]
