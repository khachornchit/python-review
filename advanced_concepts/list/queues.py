from collections import deque


def print_queue(queue):
    print("Queue:", list(queue))


def main():
    q = deque(["Eric", "John", "Michael"])
    print("Original queue:")
    print_queue(q)

    q.append("Terry")
    q.append("Graham")
    print("\nQueue after append:")
    print_queue(q)

    q.popleft()
    print("\nQueue after pop:")
    print_queue(q)

    q.popleft()
    print("\nQueue after pop:")
    print_queue(q)


if __name__ == "__main__":
    main()
