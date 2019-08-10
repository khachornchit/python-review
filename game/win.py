game = [[2, 1, 2],
        [2, 1, 2],
        [1, 2, 2],]

def get_winner():   
        win_by_row()
        win_by_col()
        win_by_diagonal()

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
                        print("Matching row ", row+1, " : ", "is the Winner !")

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
                        print("Matching column ", col+1, " : ", "is the Winner !")

# Winner by diagonal
def win_by_diagonal():
        row = 0
        col = 0
        for index in range(len(game)):
                win_forward = True
                if index == 0:
                        value = game[row][col]
                else:
                        if value != game[row+index][col+index]:
                                win_forward = False
                                break
        if win_forward == True:
                print("Matching diagonal forward is the Winner !")

        row = 0
        col = len(game[row])-1
        for index in range(len(game[row])):
                win_reverse = True
                if index == 0:
                        value = game[row][col]
                else:
                        if value != game[row+index][col-index]:
                                win_reverse = False
                                break
        if win_reverse == True:
                print("Matching diagonal reversed is the Winner !")

get_winner()