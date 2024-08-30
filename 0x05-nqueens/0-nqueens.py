#!/usr/bin/python3
"""
Solves the N-queens problem.
Finds all possible ways to place N queens on an NxN chessboard 
such that no two queens can attack each other.

Example:
    $ ./nqueens.py N
N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    possible_solutions (list): A list of lists containing all valid solutions.
Solutions are represented in the format [[row, col], [row, col], [row, col], [row, col]]
where `row` and `col` indicate the row and column positions of queens.
"""
import sys


def create_chessboard(size):
    """Create an empty chessboard of size `size`x`size`."""
    chessboard = []
    [chessboard.append([]) for _ in range(size)]
    [row.append(" ") for _ in range(size) for row in chessboard]
    return chessboard


def deep_copy_board(chessboard):
    """Return a deep copy of the chessboard."""
    if isinstance(chessboard, list):
        return list(map(deep_copy_board, chessboard))
    return chessboard


def extract_solution(chessboard):
    """Extract the solution from the chessboard into a list of queen positions."""
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_unavailable_positions(chessboard, row, col):
    """
    Mark all positions on the chessboard where queens can no longer be placed.
    This includes all horizontal, vertical, and diagonal positions.
    Args:
        chessboard (list): The current chessboard state.
        row (int): The row where the last queen was placed.
        col (int): The column where the last queen was placed.
    """
    # Mark all positions to the right
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark all positions to the left
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark all positions below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark all positions above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark diagonal positions down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark diagonal positions up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1
    # Mark diagonal positions up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark diagonal positions down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def solve_nqueens(chessboard, row, queens_count, possible_solutions):
    """
    Recursively solve the N-queens problem.
    Args:
        chessboard (list): The current chessboard state.
        row (int): The current row being worked on.
        queens_count (int): The current number of queens placed.
        possible_solutions (list): A list of valid solutions found so far.
    Returns:
        possible_solutions
    """
    if queens_count == len(chessboard):
        possible_solutions.append(extract_solution(chessboard))
        return possible_solutions

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            temp_board = deep_copy_board(chessboard)
            temp_board[row][col] = "Q"
            mark_unavailable_positions(temp_board, row, col)
            possible_solutions = solve_nqueens(
                temp_board, row + 1, queens_count + 1, possible_solutions
            )

    return possible_solutions


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

    chessboard = create_chessboard(int(sys.argv[1]))
    possible_solutions = solve_nqueens(chessboard, 0, 0, [])
    for solution in possible_solutions:
        print(solution)
