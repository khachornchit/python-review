import numpy as np


# print(np.zeros(5))
#
# print(np.zeros((3, 3)))
#
# print(np.zeros((3, 3)).tolist())


def create_zero_matrix(row, col):
    return np.zeros((row, col), dtype=int)


if __name__ == '__main__':
    matrix = create_zero_matrix(3, 3)
    # matrix[4, 4] = 1
    print(matrix)

    print('shape = ', np.shape(matrix))
    print('reshape = ', matrix.reshape(1, 9))
    print('identity = \n', np.identity(10).astype(int))
