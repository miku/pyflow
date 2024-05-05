"""
Task: Find potential improvements in the following code. Name them and suggest an alternative.

Code implements a basic TicTacToe game.
"""

import random


def check(game):
    if '.' not in game:
        return True
    if game[0] == game[1] and game[1] == game[2] and game[0] != '.':
        return True
    if game[3] == game[4] and game[4] == game[5] and game[3] != '.':
        return True
    if game[6] == game[7] and game[7] == game[8] and game[6] != '.':
        return True
    if game[0] == game[3] and game[3] == game[6] and game[0] != '.':
        return True
    if game[1] == game[4] and game[4] == game[7] and game[1] != '.':
        return True
    if game[2] == game[5] and game[5] == game[8] and game[2] != '.':
        return True
    if game[0] == game[4] and game[4] == game[8] and game[0] != '.':
        return True
    if game[2] == game[4] and game[4] == game[6] and game[2] != '.':
        return True
    return False


def print_board(board):
    print()
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])


def tic_tac_toe(board, player):
    while True:
        if not check(board):
            if player == 'x':
                pos = int(
                    input("[{}] your move [0-8]? ".format(player))
                )
            else:
                pos = random.randint(0, 8)
            if board[pos] == '.':
                board[pos] = player
                if player == "x":
                    player = "o"
                else:
                    player = "x"
                print_board(board)
        else:
            return


if __name__ == "__main__":
    board = ['.' for _ in range(9)]
    tic_tac_toe(board, "x")

