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

def update(data: array):
    """ Makes visual board off of data
    Args: Data to update
    Return: New Visual Board """
    # TODO Update better visual board

    visual_board = []
    for i in data:
        if i == 1:
            visual_board.append('X')
        elif i == 2:
            visual_board.append('O')
        else:
            visual_board.append('_')

    return visual_board

def win_check():
    # Only needs to be used 5 moves in
    pass

def menuGraphic():
    """ Print a main menu graphic
    Args: None
    Return: Main menu graphic """
    print()
    print("                                           WELCOME TO...                                          ")
    print(" ______   __     ______         ______   ______     ______          ______   ______     ______.   ")
    print("/\__  _\ /\ \   /\  ___\       /\__  _\ /\  __ \   /\  ___\        /\__  _\ /\  __ \   /\  ___\   ")
    print("\/_/\ \/ \ \ \  \ \ \____  ---  \/_/\ \/ \ \  __ \  \ \ \____ ---  \/_/\ \/ \ \ \/\ \  \ \  __\.  ")
    print("   \ \_\  \ \_\  \ \_____\         \ \_\  \ \_\ \_\  \ \_____\        \ \_\  \ \_____\  \ \_____\ ")
    print("    \/_/   \/_/   \/_____/          \/_/   \/_/\/_/   \/_____/         \/_/   \/_____/   \/_____/ ")
    print()
    print("------------------------------------------------------------------------------------------------- ")

def menuNav():
    """ Ask for user input for main menu navigation 
    Args: None
    Return: None """
    flag = True
    while flag == True:
        choice = input("What would you like to do? ")
        if choice == "play":
            pass
            #game()
            flag = False
        elif choice == "settings":
            pass
            #settings()
            flag = False
        else:
            print("Please choose something from the menu")
