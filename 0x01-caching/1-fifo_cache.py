#!/usr/bin/env python3
"""
BasicCache Module
"""
from queue import Queue

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Basic cache based on basecaching class.
    """
    def __init__(self):
        """Initialize with super class
        """
        super().__init__()
        self._fifo = Queue()

    def put(self, key, item):
        """Put the new item in cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self._fifo.put(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                a = self._fifo.get()
                print("DISCARD: {}".format(a))
                del self.cache_data[a]

    def get(self, key):
        """Get item from cache if there
        """
        return self.cache_data.get(key, None)
