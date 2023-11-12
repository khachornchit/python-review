import threading
import time

lock = threading.Lock()


def timer(name, delay, repeat):
    print(f"Timer: {name} Started")
    lock.acquire()

    print(f"{name} has acquired the lock")
    while repeat > 0:
        time.sleep(delay)
        print(f"{name}: {time.ctime(time.time())}")
        repeat -= 1
    lock.release()
    print(f"{name} has released the lock.")

    print(f"Timer: {name} Completed")


def run_timers():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 1, 5))
    t1.start()
    t2.start()

    print("Main Completed")


if __name__ == "__main__":
    run_timers()
