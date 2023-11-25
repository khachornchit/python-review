import numpy
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 5]
])

if __name__ == '__main__':
    print('np.max will find the max value by rows when using axis = 1 parameter.')
    max_values_along_rows = np.max(arr, axis=1)
    print(max_values_along_rows)

    print('np.sum will sum arr by rows when using axis=1')
    sum_by_rows = np.sum(arr, axis=1)
    print(sum_by_rows)
