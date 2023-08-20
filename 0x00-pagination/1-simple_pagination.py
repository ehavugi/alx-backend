#!/usr/bin/env python3
"""
Index_range module
"""
import csv
import math
from typing import List


from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a list with start and end index inside the data
        """
        assert(isinstance(page, int))
        assert(isinstance(page_size, int))
        assert(page > 0)
        assert(page_size > 0)
        start: int = max(page - 1, 0) * page_size + 1
        end: int = start + page_size
        with open(self.DATA_FILE) as f:
            data = f.readlines()
            if len(data) > end:
                return [x.strip().split() for x in data[start:end]]
            else:
                return []
