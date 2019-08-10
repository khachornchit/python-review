def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error ! make sure you input row/column as 0, 1, or 2  !", e)
    except Exception as e:
        print("Somthing horible !!!!")


def get_winner():
    game_won_row = win_by_row()
    game_won_col = win_by_col()
    game_won_diag = win_by_diagonal()
    return game_won_row or game_won_col or game_won_diag


def win_by_row():
    for row in range(len(game)):
        row_data = game[row]
        win_horizental = False
        for col in range(len(row_data)):
            if col > 0:
                if game[row][col] == game[row][col-1] and game[row][col] != 0:
                    win_horizental = True
                else:
                    win_horizental = False
                    break
        if win_horizental == True:
            print("Matching row ", row+1, " : ", "is the Winner !")
            return True
        else:
            return False


def win_by_col():
    for col in range(len(game[0])):
        for row in range(len(game)):
            win_vertical = False
            if row > 0:
                if game[row][col] == game[row-1][col] and game[row][col] != 0:
                    win_vertical = True
                else:
                    win_vertical = False
                    break
        if win_vertical == True:
            print("Matching column ", col+1, " : ", "is the Winner !")
            return True
        else:
            return False


def win_by_diagonal():
    row = 0
    col = 0
    for index in range(len(game)):
        win_forward = True
        if index == 0:
            value = game[row][col]
        else:
            if value != game[row+index][col+index] or value == 0:
                win_forward = False
                break
    if win_forward == True:
        print("Matching diagonal forward is the Winner !")
        return True
    else:
        return False

    row = 0
    col = len(game[row])-1
    for index in range(len(game[row])):
        win_reverse = True
        if index == 0:
            value = game[row][col]
        else:
            if value != game[row+index][col-index] or value == 0:
                win_reverse = False
                break
    if win_reverse == True:
        print("Matching diagonal reversed is the Winner !")
        return True
    else:
        return False


# Start game
play = True
players = [1, 2]

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = 1
        column_choice = int(input("What column ? [0, 1, 2] : "))
        row_choice = int(input("What row? [0, 1, 2] : "))
        game = game_board(game, current_player,
                          row_choice, column_choice)
        game_won = get_winner()
        if game_won:
            print("You are winer !")
            play = False
            break
