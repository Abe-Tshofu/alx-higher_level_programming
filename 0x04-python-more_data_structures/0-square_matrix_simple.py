#!/usr/bin/python3

der square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
