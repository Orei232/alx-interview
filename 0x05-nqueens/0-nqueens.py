#!/usr/bin/python3
"""
nqueens
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the board.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print the
    solutions.

    Args:
        N (int): The size of the chessboard.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    def format_solution(board):
        solution = []
        for row in board:
            queen_col = row.index(1)
            solution.append([board.index(row), queen_col])
        return solution

    def solve(board, col):
        if col >= N:
            solution = format_solution(board)
            print(solution)
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
