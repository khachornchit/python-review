import numpy as np


def create_custom_numpy():
    return np.array([0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    a = create_custom_numpy()
    b = create_custom_numpy()
    print(a * b)
    print('a[2:] = ', a[2:])
    print('a[:4] = ', a[:4])

    print('a[2::1] = ', a[2::1])
