import numpy as np


# print(np.zeros(5))
#
# print(np.zeros((3, 3)))
#
# print(np.zeros((3, 3)).tolist())


def create_zero_matrix(row, col):
    return np.zeros((row, col), dtype=int)


if __name__ == '__main__':
    matrix = create_zero_matrix(5, 5)
    matrix[4, 4] = 1
    print(matrix)
