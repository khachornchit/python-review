import numpy as np

game = np.array([[2, 1, 2],
                 [2, 1, 2],
                 [1, 2, 2]])


def get_winner():
    win_by_row()
    win_by_col()
    win_by_diagonal()


def check_winner(line):
    unique_elements = np.unique(line)
    if len(unique_elements) == 1 and unique_elements[0] != 0:
        print(f"Matching {line} is the Winner !")


# Winner by rows
def win_by_row():
    for row in range(len(game)):
        row_data = game[row]
        check_winner(row_data)


# Winner by columns
def win_by_col():
    for col in range(len(game[0])):
        col_data = game[:, col]
        check_winner(col_data)


# Winner by diagonal
def win_by_diagonal():
    main_diagonal = np.diagonal(game)
    anti_diagonal = np.diagonal(np.fliplr(game))

    check_winner(main_diagonal)
    check_winner(anti_diagonal)


if __name__ == '__main__':
    get_winner()
