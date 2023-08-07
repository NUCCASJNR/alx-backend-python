#!/usr/bin/python3

import asyncio

async def foo():
    print("Foo started")
    await asyncio.sleep(2)
    print("Foo completed")

async def bar():
    print("Bar started")
    await asyncio.sleep(1)
    print("Bar completed")

async def main():
    await asyncio.gather(foo(), bar())

asyncio.run(main())