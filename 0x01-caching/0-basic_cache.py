#!/usr/bin/env python3
"""
BasicCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache based on basecaching class.
    """
    def __init__(self):
        """Initialize with super class
        """
        super().__init__()

    def put(self, key, item):
        """Put the new item in cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache if there
        """
        return self.cache_data.get(key, None)
