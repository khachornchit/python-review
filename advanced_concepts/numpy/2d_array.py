#! D:\python-projects\python_chapters\numpy_env\Scripts\python.exe

import numpy as np


def create_6x5():
    result = np.array([
        [4, 0, 4, 0, 5],
        [5, 3, 2, 8, 4],
        [5, 7, 0, 0, 5],
        [3, 0, 1, 2, 8],
        [0, 7, 2, 3, 0],
        [0, 7, 2, 3, 0],
        [0, 6, 3, 3, 0],
    ])
    print(result)
    return result


def get_rows_before(np, row_index):
    result = np[:row_index]

    print("\nGet rows before row #", row_index)
    print(result)
    return result


def get_rows_after(np, row_index):
    result = np[row_index:]

    print("\nGet rows after row #", row_index)
    print(result)
    return result


if __name__ == "__main__":
    np = create_6x5()

    get_rows_before(np, 2)
    get_rows_after(np, 2)
