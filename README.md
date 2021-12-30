# Asynchronous Python Development

## Python GIL - Global Interpreter Lock
- Two threads cannot be run in one process at the same time
  - Each process in Python creates a key resource(GIL)
  - When a thread is running, it must acquire the resource
  - Since there is only one key resource per process, only one thread can run in a process at once