#!/usr/bin/python3

import asyncio

# async def add(a, b):
#     print(f"Adding {a} and {b}")
#     await asyncio.sleep(1)
#     return a + b

# async def subtract(a, b):
#     print(f"Subtracting {b} from {a}")
#     await asyncio.sleep(1)
#     return a - b

# async def multiply(a, b):
#     print(f"Multiplying {a} by {b}")
#     await asyncio.sleep(1)
#     return a * b

# async def main():
#     result_add = await add(5, 3)
#     result_subtract = await subtract(10, 4)
#     result_multiply = await multiply(6, 2)
    
#     print("Results:")
#     print(f"Addition: {result_add}")
#     print(f"Subtraction: {result_subtract}")
#     print(f"Multiplication: {result_multiply}")

import asyncio
import random

async def random_number():
    await asyncio.sleep(1)
    return random.randint(1, 100)

async def main():
    numbers = await asyncio.gather(random_number(), random_number(), random_number())
    print("Random numbers:", numbers)

asyncio.run(main())
