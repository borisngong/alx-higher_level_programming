#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_result = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squared_result[i][j] = matrix[i][j] ** 2
    return squared_result
