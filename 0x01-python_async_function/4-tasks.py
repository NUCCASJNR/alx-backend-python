#!/usr/bin/env python3

"""Asyncio Task """

import asyncio
from typing import List
task = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    Return the list of all the delays (float values) in asc order
    """
    empty = []
    for _ in range(n):
        result = await task(max_delay)
        empty.append(result)
    return sorted(empty)
