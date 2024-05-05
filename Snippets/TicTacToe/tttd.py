"""
Task: Find potential refactorings in the following code.

Code implements a basic TicTacToe game.
"""

import random
from operator import itemgetter

rows = (
    itemgetter(0, 1, 2),
    itemgetter(3, 4, 5),
    itemgetter(6, 7, 8),
)

columns = (
    itemgetter(0, 3, 6),
    itemgetter(1, 4, 7),
    itemgetter(2, 5, 8),
)

diagonals = (
    itemgetter(0, 4, 8),
    itemgetter(2, 4, 6),
)

def has_game_ended(board, empty="."):
    """
    Given a board like [" ", "x", "o", "o", "x", " ", " ", " ", " "]
    return whether this game has ended or not.
    """
    if empty not in board:
        return True
    for f in rows + columns + diagonals:
        vs = f(board)
        if all(vs[0]==e for e in vs) and vs[0] != '.':
            return True

    return False  # "false, otherwise"


def print_board(board):
    print()
    for f in rows:
        print("".join(f(board)))


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



