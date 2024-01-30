#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return [board]

    result = []

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            for solution in solve_n_queens(board, col + 1):
                result.append([row[:] for row in solution])  # Make a copy of each solution
            board[i][col] = 0

    return result

def print_solution(board):
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    board = [[0]*N for _ in range(N)]
    solutions = solve_n_queens(board, 0)
    if not solutions:
        print("Solution does not exist")
        sys.exit(1)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()

