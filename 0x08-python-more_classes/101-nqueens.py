#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1) is True:
                return True
            board[i][col] = 0
    return False


def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()


def main():
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    board = [[0]*N for _ in range(N)]
    if solve_n_queens(board, 0) is False:
        print("Solution does not exist")
        sys.exit(1)

    print_solution(board)


if __name__ == "__main__":
    main()
