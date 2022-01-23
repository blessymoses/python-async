"""
   Download all sites - non concurrent
"""
import time

import requests


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = ["https://github.com/blessymoses", "https://github.com/coding-gc"] * 100
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(
        f"Downloaded {len(sites)} sites in {duration} seconds"
    )  # Downloaded 200 sites in 3.236158847808838 seconds
