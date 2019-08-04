tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print("tel : ", tel)

print("tel['jack] : ", tel['jack'])

del tel['sape']
tel['irv'] = 4127
print("tel : ", tel)

print("list(tel.keys()) : ", list(tel.keys()))

print("sorted(tel.keys()) : ", sorted(tel.keys()))

print("'guido' in tel : ", 'guido' in tel)

print("'jack' not in tel : ", 'jack' not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs
dictKeyValue = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dictKeyValue)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dictSimpleKey = dict(sape=4139, guido=4127, jack=4098)
print(dictSimpleKey)

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
dictArbitary = {x: x**2 for x in (2, 4, 6)}
print(dictArbitary)