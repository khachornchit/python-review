game = [[1, 1, 1],
        [0, 0, 0],
        [2, 2, 0]]

def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0 :
            print("Winner !")

win(game)