#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix is None:
        matrix = []
    return list(map(lambda row: list(map(lambda a: pow(a, 2), row)), matrix))
