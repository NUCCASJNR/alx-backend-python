#!/usr/bin/python3

import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    results = []

    for url in urls:
        data = await fetch_url(url)
        results.append(data)
    print(results)

asyncio.run(main())
