def demonstrate_dictionary_operations():
    telephone_directory = {'jack': 4098, 'sape': 4139, 'guido': 4127}
    print("telephone_directory:", telephone_directory)

    print("telephone_directory['jack]:", telephone_directory['jack'])

    del telephone_directory['sape']
    telephone_directory['irv'] = 4127
    print("telephone_directory:", telephone_directory)

    print("list(telephone_directory.keys()):", list(telephone_directory.keys()))

    print("sorted(telephone_directory.keys()):", sorted(telephone_directory.keys()))

    print("'guido' in telephone_directory:", 'guido' in telephone_directory)

    print("'jack' not in telephone_directory:", 'jack' not in telephone_directory)

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs
    dict_key_value = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dict_key_value)

    # When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
    dict_simple_key = dict(sape=4139, guido=4127, jack=4098)
    print(dict_simple_key)

    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
    dict_arbitrary = {x: x ** 2 for x in (2, 4, 6)}
    print(dict_arbitrary)


if __name__ == "__main__":
    demonstrate_dictionary_operations()
