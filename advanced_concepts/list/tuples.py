def print_hello_universe():
    print("Hello universe")


def demonstrate_tuple():
    programming_languages = "Python", "Java", "C++", "C#"

    print("\nType of programming_languages:", type(programming_languages))
    print("Programming languages:", programming_languages)

    print("\nIterating through programming_languages:")
    for language in programming_languages:
        print(language)

    t = 12345, 54321, 'hello!'
    print("\nTuple t:", t)
    print("First element of t:", t[0])

    u = t, (1, 2, 3, 4, 5)
    print("\nTuple u:", u)
    print("First element of t (still the same):", t[0])


def main():
    print_hello_universe()
    demonstrate_tuple()


if __name__ == "__main__":
    main()
