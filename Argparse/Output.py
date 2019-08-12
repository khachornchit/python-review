import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
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
    print("The "+str(args.num)+"th fib number is "+str(fib(args.num)))

    if args.output:
        file = open("./Argparse/data.txt", "a")
        file.write(
            "The "+str(args.num)+"th fib number is " + str(fib(args.num))+"\n")


if __name__ == '__main__':
    Main()
