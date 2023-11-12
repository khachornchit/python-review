import argparse
import os


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        help="Add an argument type of integer for calculation.",
        type=int)

    parser.add_argument(
        "-o", "--output",
        help="Add a parameter -o to save the result to the file fiboacci.txt",
        action="store_true")

    args = parser.parse_args()
    result = fib(args.num)
    print(f"The {args.num}th fib number is {result}")

    if args.output:
        file_path = os.path.join("argparse", "data.txt")
        with open(file_path, "a") as file:
            file.write(f"The {args.num}th fib number is {result}\n")


if __name__ == '__main__':
    main()
