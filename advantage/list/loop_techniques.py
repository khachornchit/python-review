def print_knights(knights):
    for key, value in knights.items():
        print(key, value)


def enumerate_example():
    for index, value in enumerate(['tic', 'tac', 'toe']):
        print(index, value)


def zip_example():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']

    for question, answer in zip(questions, answers):
        print('What is your {0}? It is {1}.'.format(question, answer))


def reversed_example():
    for i in reversed(range(1, 10, 2)):
        print(i)


def sorted_example():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for fruit in sorted(set(basket)):
        print(fruit)


def loop_over_slice_copy():
    words = ['cat', 'window', 'defenestrate']
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    print(words)


def main():
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    print_knights(knights)

    enumerate_example()
    zip_example()
    reversed_example()
    sorted_example()
    loop_over_slice_copy()


if __name__ == "__main__":
    main()
