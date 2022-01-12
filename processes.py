"""
Multiprocessing
"""
import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user: {time.time() - start}")


def do_calculation():
    start = time.time()
    print("Started calculating...")
    [x ** 2 for x in range(20000000)]
    print(f"do_calculation: {time.time() - start}")


start = time.time()
ask_user()
do_calculation()
print(f"Single thread execution: {time.time() - start}")

# process
process = Process(target=do_calculation)
process.start()

start = time.time()
ask_user()
process.join()
print(f"Process execution: {time.time() - start}")
