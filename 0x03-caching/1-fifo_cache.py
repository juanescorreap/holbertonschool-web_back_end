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
        if key is None or item is None:
            pass
        elif len(self.cache_data) >= self.MAX_ITEMS:
            keys_list = list(self.cache_data)
            key_to_delte = keys_list[0]
            print("DISCARD: {}".format(key_to_delte))
            del self.cache_data[key_to_delte]
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)