def print_stack(stack):
    print("Stack:", stack)


def main():
    stack = [3, 4, 5]
    print("Original stack:")
    print_stack(stack)

    stack.append(6)
    stack.append(7)
    print("\nStack after append:")
    print_stack(stack)

    stack.pop()
    print("\nStack after stack.pop():")
    print_stack(stack)

    stack.pop()
    print("\nStack after stack.pop():")
    print_stack(stack)


if __name__ == "__main__":
    main()
