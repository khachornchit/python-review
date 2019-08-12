game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error ! something went wrong ! ", e)
    except Exception as e:
        print("Somthing horible !!!!")
    else:
        print("else")   
    finally:
        print("finally")

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, col=1)
game = game_board(game_board, player=1, row=3, col=1)
