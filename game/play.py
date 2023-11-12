import numpy as np
from colorama import init, Fore, Back, Style

init(autoreset=True)


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, end=" ")
            for item in row:
                if item == 0:
                    print(Fore.GREEN + Back.GREEN + Style.BRIGHT + "  ", end="")
                elif item == 1:
                    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + f" X{' '}", end="")
                elif item == 2:
                    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + f" O{' '}", end="")
            print(Style.RESET_ALL)
        return game_map
    except IndexError as e:
        print("Error! Make sure you input row/column as 0, 1, or 2!", e)
        return False
    except Exception as e:
        print("Something horrible happened!", e)
        return False


def check_winner(game):
    return win_by_row(game) or win_by_col(game) or win_by_diagonal(game)


def win_by_row(game):
    for row in range(len(game)):
        row_data = game[row]
        if all(cell == row_data[0] and cell != 0 for cell in row_data):
            print(Fore.GREEN + f"Matching row {row + 1} is the Winner!" + Style.RESET_ALL)
            return True
    return False


def win_by_col(game):
    for col in range(len(game[0])):
        col_data = [game[row][col] for row in range(len(game))]
        if all(cell == col_data[0] and cell != 0 for cell in col_data):
            print(Fore.GREEN + f"Matching column {col + 1} is the Winner!" + Style.RESET_ALL)
            return True
    return False


def win_by_diagonal(game):
    main_diagonal = [game[i][i] for i in range(len(game))]
    anti_diagonal = [game[i][len(game) - 1 - i] for i in range(len(game))]

    if all(cell == main_diagonal[0] and cell != 0 for cell in main_diagonal):
        print(Fore.GREEN + "Matching diagonal forward is the Winner!" + Style.RESET_ALL)
        return True
    elif all(cell == anti_diagonal[0] and cell != 0 for cell in anti_diagonal):
        print(Fore.GREEN + "Matching diagonal reversed is the Winner!" + Style.RESET_ALL)
        return True
    return False


def main():
    play = True

    while play:
        game = np.zeros((3, 3), dtype=int)

        game_won = False
        game = game_board(game, just_display=True)
        while not game_won:
            current_player = 1
            column_choice = int(input("What column? [0, 1, 2]: "))
            row_choice = int(input("What row? [0, 1, 2]: "))
            game = game_board(game, current_player, row_choice, column_choice)
            game_won = check_winner(game)
            if game_won:
                print(Fore.GREEN + "You are the winner!" + Style.RESET_ALL)
                again = input("The game is over! Would you like to play again? [y/n]: ")
                if again.lower() == 'y':
                    print("Restarting...")
                else:
                    print("Byeeeeee :)")
                    play = False
                    break


if __name__ == '__main__':
    main()
