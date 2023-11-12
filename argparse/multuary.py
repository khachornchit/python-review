import argparse
from string import Template
import os


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument(
        "num",
        help="Add an argument type of integer for calculation.",
        type=int)

    parser.add_argument(
        "-o", "--output",
        help="Add a parameter -o to save the result to the file fiboacci.txt",
        action="store_true")

    args = parser.parse_args()
    data = dict(num=args.num, result=fib(args.num))

    if args.verbose:
        template = Template("The $num fibonacci number is $result")
        print(template.substitute(data))
    elif args.quiet:
        template = Template("$num")
        print(template.substitute(data))
    else:
        template = Template("fibonacci($num) = $result")
        print(template.substitute(data))

    if args.output:
        file_path = os.path.join("argparse", "data.txt")
        with open(file_path, "a") as file:
            file.write(f"The {args.num}th fib number is {fib(args.num)}\n")


if __name__ == '__main__':
    main()
