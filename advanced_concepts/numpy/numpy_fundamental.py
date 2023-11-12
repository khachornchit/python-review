#! D:\python-projects\python_chapters\numpy_env\Scripts\python.exe

import numpy as np

arrange = np.arange(6)

arr = np.array([
    [0, 1, 2, 3, 4, 5, 6], 
    [7, 8, 9, 10, 11, 12, 13]
])

print("arrange: \n", arrange)
print("arr: \n", arr)
print("arr shape: \n", arr.shape)
print("arr dimension: \n", arr.ndim)
print("arr dimension: \n", arr.dtype)
print("Specific column:", arr[:, 2])
print("Specific row:", arr[1, :])
print("a[start-index:end-index:step-size]:", arr[0, 1:-1:2])

print('Multiply array:')
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a*b

print('a: ', a)
print('b: ', b)
print('c: ', c)

arr6 = np.array([np.arange(6), np.arange(6), np.arange(6), np.arange(6), np.arange(6), np.arange(6)])
print('Array 6x6:')
print(arr6)

print('All 0 matrix')
print(np.zeros((2, 3)))
print("\n")
print(np.zeros((2, 3, 3)))

print('All 1 matrix')
print(np.ones((4, 2, 2)))

print('Any other number')
print(np.full((2,22), 27))

print('Any other number')
print(np.full_like(arr, 4))

# Random Matrix
print(np.random.randint(7, size=(3, 3)))

# Identify Matrix
print(np.identity(5))

# Matrix Solutions
output = np.ones((5, 5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:-1, 1:-1]=z
print(output)

# Copy
bbb= arr.copy()
bbb[0, 0]=500
print(bbb)

# Reorganizing Arrays
before = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(before)

after = before.reshape(1, 8)
print(after)

print(np.all(before > 2, axis=1))

print((before >=2) & (before<=5))