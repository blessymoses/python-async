import time
from threading import Thread


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

thread1 = Thread(target=do_calculation)
# thread2 = Thread(target=ask_user)
thread2 = Thread(target=do_calculation)


start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"Multi thread execution: {time.time() - start}")
