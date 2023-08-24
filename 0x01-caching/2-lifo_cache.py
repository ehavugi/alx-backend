#!/usr/bin/env python3
"""
BasicCache Module
"""
from queue import LifoQueue

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Basic cache based on basecaching class.
    LIFO based replacement policy
    """
    def __init__(self):
        """Initialize with super class
        """
        super().__init__()
        self._lifo = LifoQueue()

    def put(self, key, item):
        """Put the new item in cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                a = self._lifo.get()
                print("DISCARD: {}".format(a))
                del self.cache_data[a]
            self._lifo.put(key)

    def get(self, key):
        """Get item from cache if there
        """
        return self.cache_data.get(key, None)
