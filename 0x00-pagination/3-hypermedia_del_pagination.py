#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        return a dictionary with following keys, page_size, page, data,
        next_page,next_page,total_pages
        """
        assert(isinstance(page, int))
        assert(isinstance(page_size, int))
        assert(page > 0)
        assert(page_size > 0)

        data: Dict = {}
        returnedData = self.get_page(page, page_size)

        data['page_size'] = len(returnedData)
        data['page'] = page
        data['data'] = returnedData
        if len(returnedData) == 0:
            data['next_page'] = None
        else:
            data['next_page'] = page + 1
        if page > 1:
            data['prev_page'] = page - 1
        else:
            data['prev_page'] = None
        data['total_pages'] = len(self.dataset())
        return data

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """use index dataset.
        """
        page = index
        if page is None:
            page = 0
        assert(page < len(self.indexed_dataset()))
        assert(isinstance(page_size, int))
        assert(page >= 0)
        assert(page_size > 0)

        data: Dict = {}
        All = self.indexed_dataset()
        start = max(page - 1, 0)

        returnedData = [All[x] for x in All if
                        (x >= start and x < start + page_size)]

        data['index'] = start + 1

        if len(returnedData) == 0:
            data['next_index'] = None
        else:
            data['next_index'] = data['index'] + page_size
        data['page_size'] = len(returnedData)
        data['data'] = returnedData
        return data
