"""Download all sites - using asyncio
"""
import asyncio
import time

import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = ["https://github.com/blessymoses", "https://github.com/coding-gc"] * 100
    start_time = time.time()
    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(
        f"Downloaded {len(sites)} sites in {duration} seconds"
    )  # Downloaded 200 sites in 0.25416088104248047 seconds
