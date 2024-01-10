#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = [[0 for _ in range(len(matrix[0]))]
                 for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sq_matrix[i][j] = matrix[i][j] ** 2
    return(sq_matrix)


if __name__ == "__main__":
    square_matrix_simple(matrix)
