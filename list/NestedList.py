matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix)

print("transposed matrix  : ", [[col[i] for col in matrix] for i in range(4)])

print("use zip() function : ", list(zip(*matrix)))

