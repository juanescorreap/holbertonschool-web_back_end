#!/usr/bin/env python3
"""
Class LRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.record_of_keys = []

    def put(self, key, item):
        """
        Method to assign to the dictionary
        self.cache_data the item value for the key
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            key_to_delte = self.record_of_keys.pop(0)
            del self.cache_data[key_to_delte]
            print("DISCARD: {}".format(key_to_delte))
        self.record_of_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Method to return the value in
        self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.record_of_keys.remove(key)
            self.record_of_keys.append(key)
            return self.cache_data.get(key)
