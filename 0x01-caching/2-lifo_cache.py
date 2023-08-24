#!/usr/bin/env python3
"""
BasicCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Basic cache based on basecaching class.
    LIFO based replacement policy
    """
    def __init__(self):
        """
        Initialize with super class.
        Initialize super class and new lifo queu
        """
        super().__init__()
        self._lifo = []

    def put(self, key, item):
        """Put the new item in cache using lifo
        replacement policy
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                a = self._lifo.pop(len(self._lifo) - 1)
                print("DISCARD: {}".format(a))
                del self.cache_data[a]
            self._lifo.append(key)

    def get(self, key):
        """Get item from cache if there
        it returns a match or None
        """
        return self.cache_data.get(key, None)
