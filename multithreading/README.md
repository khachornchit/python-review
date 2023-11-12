# Multithreading in Python

This directory contains Python scripts showcasing multithreading concepts, including asynchronous file writing, thread
synchronization using locks, and creating timers with threading.

## 1. async_write.py

### Asynchronous File Write with Threading

This Python script demonstrates asynchronous file writing using threading. It collects user input, performs a background
file write in a separate thread, and allows the main program to continue execution.

#### Usage

1. Run the script `async_write.py`.
2. Enter a string when prompted.
3. The program will continue to execute while writing the input to a file in the background.
4. After completing the background thread, the program will display the result of a calculation.

#### Technology Stack

- Python 3.7.3
- Threading Module

#### Miscellaneous

- The file 'out.txt' is used for storing the user input.

## 2. lock.py

### Threading with Lock

This Python script demonstrates the use of threading with a lock. It includes a timer function that runs in separate
threads, acquiring and releasing a lock during execution.

#### Usage

1. Run the script `lock.py`.
2. The program will start two timers in separate threads.
3. Each timer will acquire a lock, execute for a specified duration, release the lock, and print the completion message.

#### Technology Stack

- Python 3.7.3
- Threading Module

#### Miscellaneous

- The script uses a lock to synchronize access to shared resources.

## 3. timer.py

### Timer with Threading

This Python script demonstrates the use of threading for creating timers. It launches two timers in separate threads.

#### Usage

1. Run the script `timer.py`.
2. The program will start two timers in separate threads.
3. Each timer will execute for a specified duration and print messages.

#### Technology Stack

- Python 3.7.3
- Threading Module

#### Miscellaneous

- The script uses the threading module to create timers.
