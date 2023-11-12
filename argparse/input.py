import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser(description="Calculate the nth Fibonacci number.")
    parser.add_argument("num", type=int,
                        help="An integer specifying the position of the Fibonacci number to be calculated.")

    args = parser.parse_args()
    fib_number = fib(args.num)
    print(f"The {args.num}th Fibonacci number is {fib_number}")


if __name__ == '__main__':
    main()
