#!/usr/bin/env python3
"""0. Basic dictionary"""
from base_caching import BaseCaching
from typing import Union


class BasicCache(BaseCaching):
    """Defines Basic caching operations"""

    def put(self, key: str, item: str) -> None:
        """Assigns the item to the key in `self.cache_data`"""

        if None in (key, item):
            return

        self.cache_data[key] = item

    # ______________________________________________________________________

    def get(self, key: str) -> Union[None, str]:
        """Gets an items from `self.cache_data`"""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
