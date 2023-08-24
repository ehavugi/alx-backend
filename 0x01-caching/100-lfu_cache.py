#!/usr/bin/env python3
"""
BasicCache Module
"""
from queue import Queue

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Basic cache based on basecaching class.
    """
    def __init__(self):
        """Initialize with super class
        """
        super().__init__()
        self._used = {}
        self._freq = {}
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
                datai = sorted(self._freq.items(), key=lambda x: x[1],
                               reverse=False)
                a = datai[0][0]
                temp = []
                for i in self.cache_data.values():
                    if i == datai[0][1]:
                        temp.append(i)
                if len(temp) <= 1:
                    print("DISCARD: {}".format(a))
                else:
                    a_ = a
                    a_v_ = data[0][1]
                    for a_k, a_v in self._usage.items():
                        if a_v < a_v_:
                            a_v_ = a_v
                            a_ = a
                    print("DISCARD: {} ".format(a_))
                    a = a_
                del self.cache_data[a]
                del self._used[a]
                del self._freq[a]
            self.cache_data[key] = item
            self._usage += 1
            self._used[key] = self._usage
            self._freq[key] = self._freq.get(key, 0) + 1

    def get(self, key):
        """Get item from cache if there
        """
        if self.cache_data.get(key, None):
            self._usage += 1
            self._used[key] = self._usage
            self._freq[key] = self._freq.get(key, 0) + 1
        return self.cache_data.get(key, None)
