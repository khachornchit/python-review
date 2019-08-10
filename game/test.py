game = [[2, 0, 1],
        [1, 0, 1],
        [2, 2, 1],]

print("len(game) : ", len(game))
print("range(len(game)) : ", range(len(game)))

print('range function ...')
for i in range(len(game)):
    print(i)

print('enumerate function')
for count, row in enumerate(game):
        print(count, ' : ', row)