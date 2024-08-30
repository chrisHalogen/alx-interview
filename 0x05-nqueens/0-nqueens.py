#!/usr/bin/python3
"""Module to solve the N-Queens problem.
"""
import sys

results = []
"""Stores all the potential solutions to the N-Queens problem.
"""
board_size = 0
"""Represents the dimension of the chessboard.
"""
positions = None
"""Holds all possible queen positions on the chessboard.
"""


def fetch_input():
    """Fetches and validates the command-line argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def queens_in_conflict(queen1, queen2):
    """Determines if two queens can attack each other.

    Args:
        queen1 (list or tuple): The position of the first queen.
        queen2 (list or tuple): The position of the second queen.

    Returns:
        bool: True if the queens can attack each other, False otherwise.
    """
    if (queen1[0] == queen2[0]) or (queen1[1] == queen2[1]):
        return True
    return abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])


def solution_exists(candidate):
    """Checks if a particular configuration is already in the list of results.

    Args:
        candidate (list of lists): A possible arrangement of queens.

    Returns:
        bool: True if the configuration already exists, False otherwise.
    """
    global results
    for existing in results:
        match_count = 0
        for existing_pos in existing:
            for candidate_pos in candidate:
                if (
                    existing_pos[0] == candidate_pos[0]
                    and existing_pos[1] == candidate_pos[1]
                ):
                    match_count += 1
        if match_count == board_size:
            return True
    return False


def construct_solution(row, candidate):
    """Constructs and stores valid solutions to the N-Queens problem.

    Args:
        row (int): The current row being considered on the chessboard.
        candidate (list of lists): The current candidate solution.
    """
    global results
    global board_size
    if row == board_size:
        solution_copy = candidate.copy()
        if not solution_exists(solution_copy):
            results.append(solution_copy)
    else:
        for col in range(board_size):
            pos_index = (row * board_size) + col
            queen_conflicts = zip(
                list([positions[pos_index]]) * len(candidate), candidate
            )
            has_conflict = map(
                lambda x: queens_in_conflict(x[0], x[1]), queen_conflicts
            )
            candidate.append(positions[pos_index].copy())
            if not any(has_conflict):
                construct_solution(row + 1, candidate)
            candidate.pop(len(candidate) - 1)


def find_solutions():
    """Generates all valid solutions for the given chessboard size."""
    global positions, board_size
    positions = list(
        map(lambda x: [x // board_size, x % board_size], range(board_size**2))
    )
    start_row = 0
    candidate_positions = []
    construct_solution(start_row, candidate_positions)


board_size = fetch_input()
find_solutions()
for result in results:
    print(result)
