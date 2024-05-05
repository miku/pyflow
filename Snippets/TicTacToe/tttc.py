"""
Task: Find potential refactorings in the following code.

Code implements a basic TicTacToe game.
"""

import random


def has_game_ended(board, empty="."):
    """
    Given a board like [" ", "x", "o", "o", "x", " ", " ", " ", " "]
    return whether this game has ended or not.
    rows = 012, 345, 678
    cols = 036, 147, 258
    diag = 048, 246
    """
    # draw
    if empty not in board:
        return True
    # rows
    if board[0] == board[1] and board[1] == board[2] and board[0] != empty:
        return True
    if board[3] == board[4] and board[4] == board[5] and board[3] != empty:
        return True
    if board[6] == board[7] and board[7] == board[8] and board[6] != empty:
        return True

    # columns
    if board[0] == board[3] and board[3] == board[6] and board[0] != empty:
        return True
    if board[1] == board[4] and board[4] == board[7] and board[1] != empty:
        return True
    if board[2] == board[5] and board[5] == board[8] and board[2] != empty:
        return True

    # diagonals
    if board[0] == board[4] and board[4] == board[8] and board[0] != empty:
        return True
    if board[2] == board[4] and board[4] == board[6] and board[2] != empty:
        return True

    return False  # "false, otherwise"


def print_board(board):
    print()
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])


def tic_tac_toe(board, player, human="x", empty="."):
    while not has_game_ended(board):
        if player == human:
            pos = int(
                input("[{}] your move [0-8]? ".format(player))
            )
        else:
            pos = random.randint(0, 8)
        if board[pos] != empty:
            continue
        board[pos] = player
        player = "o" if player == "x" else "x"
        print_board(board)


if __name__ == "__main__":
    empty = "."
    board = [empty for _ in range(9)]  # [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "x"
    tic_tac_toe(board, player)



