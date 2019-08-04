game = "Hello world"
print(id(game))


def game_board(player=0, row=0, col=0, just_display=False):
    global game
    game = "Change !"
    print(id(game))
    print(game)


print(game)
game_board()
print(game)
print(id(game))
