#!/usr/bin/python3
"""N-Queens puzzle solver module.
Finds all valid solutions for placing N non-attacking
queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N should be an integer greater than or equal to 4.
Attributes:
    board (list): A 2D list representing the chessboard.
    solutions (list): A list of all found solutions.
Each solution is represented as [[r, c], [r, c], [r, c], [r, c]],
where `r` and `c` are the row and column indices of each queen on the board.
"""
import sys


def init_board(n):
    """Creates an `n`x`n` chessboard initialized with spaces."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    """Returns a deep copy of the chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Extracts the solution from the chessboard in list format."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """Marks the attacked positions on the chessboard.
    Marks all positions that are attacked by the last placed queen.
    Args:
        board (list): The current state of the chessboard.
        row (int): The row index of the last placed queen.
        col (int): The column index of the last placed queen.
    """
    # Mark all spots to the right
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all spots to the left
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively attempts to solve the N-Queens puzzle.
    Args:
        board (list): The current state of the chessboard.
        row (int): The current row being processed.
        queens (int): The current number of queens placed on the board.
        solutions (list): A list to store all valid solutions.
    Returns:
        solutions: The list of all valid solutions found.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
