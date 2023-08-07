#!/usr/bin/env python3

"""
Multiple Coroutines
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    Return the list of all the delays (float values) in asc order
    """
    empty = []
    for _ in range(n):
        result = await wait_random(max_delay)
        empty.append(result)
    return sorted(empty)
