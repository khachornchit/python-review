game = [[2, 0, 1],
        [2, 0, 0],
        [2, 2, 0],]

check = []

for row in game:
        check.append(row[0])
        print(check.count(check[0]), " - ", len(check))
