a = [-1, 1, 66.25, 333, 333, 1234.5]

print("a original       : ", a)

del a[0]
print("a after del a[0] : ", a)

del a[2:4] # between 2 - 4
print("a after del a[2:4] : ", a)

del a[:] # empty array
print("a after del a[:] : ", a)

del a # delete entire variable
print("a after del a : ", a)