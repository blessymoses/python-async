# Asynchronous Python Development

## Python GIL - Global Interpreter Lock
- Two threads cannot be run in one process at the same time
  - Each process in Python creates a key resource(GIL)
  - When a thread is running, it must acquire the resource
  - Since there is only one key resource per process, only one thread can run in a process at once

## When to use concurrency

- IO bound
  - general rule of thumb is to use `asyncio` when you can, `threading` when you must.
  - `threading` is better for IO-bound tasks.
- CPU bound
  - CPU-bound problems only really gain from using `multiprocessing`.
  - `threading` and `asyncio` do not help this type of problem at all.
  - Multiprocessing is well-suited for CPU-bound tasks such as, tightly bound `for loops` and mathematical computations.

  ## async IO
  - async IO is a single-threaded, single-process design: it uses cooperative multitasking.
  - async IO gives a feeling of concurrency despite using a single thread in a single process. 
  - Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.
  - `asynchronous`
    - Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
    - Asynchronous code facilitates concurrent execution.
    