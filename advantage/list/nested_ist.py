import numpy as np


def print_matrix(matrix):
    for row in matrix:
        print(row)


def transpose_matrix(matrix):
    return [[col[i] for col in matrix] for i in range(len(matrix[0]))]


def transpose_matrix_np(matrix):
    return np.transpose(matrix)


def main():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print("Original matrix:")
    print_matrix(matrix)

    transposed_matrix = transpose_matrix(matrix)
    print("\nTransposed matrix:")
    print_matrix(transposed_matrix)

    transposed_matrix_np = transpose_matrix_np(matrix)
    print("\nTransposed matrix using NumPy:")
    print(transposed_matrix_np)

    # Alternatively, using the built-in zip function
    print("\nTransposed matrix using zip:")
    print(list(zip(*matrix)))


if __name__ == "__main__":
    main()
