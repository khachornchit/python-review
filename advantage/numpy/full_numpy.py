import numpy as np


def create_full_numpy(row, col):
    return np.full((row, col), 5)


if __name__ == '__main__':
    print(create_full_numpy(5, 5))
