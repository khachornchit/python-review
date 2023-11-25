import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 5]
])

if __name__ == '__main__':
    print('np.max will find the maximum value along column when using axis = 0 parameter.')
    max_values_along_columns = np.max(arr, axis=0)
    print(max_values_along_columns)

    print('np.sum will sum arr by column when using axis=0')
    print(np.sum(arr, axis=0))
