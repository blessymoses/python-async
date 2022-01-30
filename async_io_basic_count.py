"""asyncio
   uses cooperative multitasking: The tasks must cooperate by announcing when they are ready to be switched out
"""
import asyncio
import time


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
"""
One
One
One
Two
Two
Two
/Users/blessy/Documents/myrepo/python-async/async_io_basic_count.py executed in 1.00 seconds
"""
