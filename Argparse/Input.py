import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num",
                        help="Please add an argument as a type of integer number for calculation.",
                        type=int)

    args = parser.parse_args()
    print("The "+str(args.num)+"th fib number is "+str(fib(args.num)))


if __name__ == '__main__':
    Main()
