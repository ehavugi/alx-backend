#!/usr/bin/env python3
"""
Generate start index and end index correponding to
page and page_size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start and end index given a page and  page size.
    """
    start: int = max(page - 1, 0) * page_size
    end: int = start + page_size
    return (start, end)
