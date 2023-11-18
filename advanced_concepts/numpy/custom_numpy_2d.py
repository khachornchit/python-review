#! D:\python-projects\python_chapters\numpy_env\Scripts\python.exe

import numpy as np


def create_6x5():
    return np.array([
        [4, 0, 4, 0, 5],
        [5, 3, 2, 8, 4],
        [5, 7, 0, 0, 5],
        [3, 0, 1, 2, 8],
        [0, 7, 2, 3, 0],
        [0, 7, 2, 3, 0],
        [0, 6, 3, 3, 0],
    ])


if __name__ == "__main__":
    matrix = create_6x5()
    # print(matrix)
    print(matrix[0:3, 0:3])
