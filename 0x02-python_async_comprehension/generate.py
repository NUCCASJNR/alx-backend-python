#!/usr/bin/env python3

# n = 'Hello'
# for _ in range(5):
#     print(n)

import asyncio


async def async_odd_generator(number):
    for i in range(number):
        if i % 2 != 0:
            await asyncio.sleep(1)
            yield f"Data {i}"

async def even(number):
    for i in range(number):
         if i % 2 == 0:
            await asyncio.sleep(1)
            yield f"Data {i}"

async def main():
    async for data in async_odd_generator(10):
        print(data)
    async for data in even(10):
        print(data)
asyncio.run(main())
