#!/usr/bin/env python3
"""
Class FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Method to assign to the dictionary
        self.cache_data the item value for the key
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            keys_list = list(self.cache_data)
            key_to_delte = keys_list[0]
            print("DISCARD: {}".format(key_to_delte))
            del self.cache_data[key_to_delte]

    def get(self, key):
        """
        Method to return the value in
        self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
