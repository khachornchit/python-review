import itertools

x = [1, 2, 3, 4]
n = itertools.cycle(x)

print(next(n))
print(next(n))