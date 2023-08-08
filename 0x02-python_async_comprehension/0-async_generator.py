#!/usr/bin/env python3

"""
Async Generator
"""
import asyncio
from typing import List
from random import uniform


async def async_generator() -> List[float]:
    """
    coroutine loops 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
