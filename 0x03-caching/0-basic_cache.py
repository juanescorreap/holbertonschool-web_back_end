#!/usr/bin/env python3
"""
Class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class BasicCache that inherits from
    BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Method to assign to the dictionary
        self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method to return the value in
        self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
