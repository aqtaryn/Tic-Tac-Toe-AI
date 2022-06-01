""" A file for most supporting functions 
    Please add tests for functions added in the testing.py file """

from numpy import array



def print_board(board: array):
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array

def take_move(data: array, player: int, move: int):
    """ Get user input, check if valid and update data if True
    Args: Data of board, which players move (1 == 'X', 2 == 'O'),
    Return: Updated board data """
    if data[move-1] == 0:
        data[move-1] = player
    return data

def update():
    """ Update data for game to use 
    Args: Data to update, Board(s) to update
    Return: Updated Board(s) """
    pass

def win_check():
    import main as m


    winner = None
    #horizontal winner
    def horizontalwin(board):
        global winner
        if board[0] == board[1] == board[2] and board[0]!= " ":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != " ":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6]!= " ":
            winner = board[6]
            return True
    #vertical winner
    def verticalwin(board):
        global winner
        if board[0] == board[3] == board[6] and board[0]!= " ":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != " ":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2]!= " ":
            winner = board[2]
            return True
    #diagonal winner
    def diagonalwin(board):
        global winner
        if board[0] == board[4] == board[8] and board[0]!= " ":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != " ":
            winner = board[2]
            return True
    #checks if is a cat game
    def nowin(board):
        if " " not in board:
            print(m.visual_board)
            print("There was no winner :(")
            quit()

    def display_winner(board):
        global winner
        if horizontalwin(board) or verticalwin(board) or diagonalwin(board):
            print("The winner is {}".format(winner))
