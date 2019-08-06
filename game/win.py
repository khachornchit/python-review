game = [[2, 2, 2],
        [2, 2, 2],
        [2, 2, 2],]

# Winner by rows
def win_by_row():
        for row in range(len(game)):
                row_data = game[row]
                win_horizental = False
                for col in range(len(row_data)):
                        if col > 0:
                                if game[row][col] == game[row][col-1]:
                                        win_horizental = True
                                else:
                                        win_horizental = False
                                        break
                if win_horizental == True:
                        print("row ", row+1, " : ", "is the Winner !")

# Winner by columns
def win_by_col():
        for col in range(len(game[0])):
                for row in range(len(game)):
                        win_vertical = False
                        if row > 0:
                                if game[row][col] == game[row-1][col]:
                                        win_vertical = True
                                else:
                                        win_vertical = False
                                        break
                if win_vertical == True:
                        print("Column ", col+1, " : ", "is the Winner !")

# Winner by diagonal
def win_by_diagonal():
        row = 0
        col = 0
        if game[row][col] == game[row+1][col+1] == game[row+2][col+2]:
                print("Diagonal forward is the Winner !")
        row = 0
        col = 2
        if game[row][col] == game[row+1][col-1] == game[row+2][col-2]:
                print("Diagonal reversed is the Winner !")

def get_winner():   
        win_by_row()
        win_by_col()
        win_by_diagonal()

get_winner()