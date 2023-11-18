import numpy as np


def create_dict():
    return {'Capital': "London", 'Food': "Fish&Chips", '2012': "Olympics"}


def create_list_from_dict(data):
    return [[k, v] for k, v in data.items()]


def create_numpy_from_list(data):
    return np.array(data)


if __name__ == '__main__':
    dict_info = create_dict()
    list_info = create_list_from_dict(dict_info)
    np1 = create_numpy_from_list(list_info)
    print(np1)
