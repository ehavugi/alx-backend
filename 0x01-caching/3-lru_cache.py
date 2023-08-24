#!/usr/bin/env python3
"""
BasicCache Module
"""
from queue import Queue

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Basic cache based on basecaching class.
    """
    def __init__(self):
        """Initialize with super class
        """
        super().__init__()
        self._used = {}
        self._usage = 0

    def put(self, key, item):
        """Put the new item in cache
        """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                self.cache_data[key] = item
            elif len(self.cache_data) + 1 > self.MAX_ITEMS:
                datai = sorted(self._used.items(), key=lambda x: x[1],
                               reverse=False)
                a = datai[0][0]
                print("DISCARD: {}".format(a))
                del self.cache_data[a]
                del self._used[a]
            self.cache_data[key] = item
            self._usage += 1
            self._used[key] = self._usage

    def get(self, key):
        """Get item from cache if there
        """
        if self.cache_data.get(key, None):
            self._usage += 1
            self._used[key] = self._usage
        return self.cache_data.get(key, None)
