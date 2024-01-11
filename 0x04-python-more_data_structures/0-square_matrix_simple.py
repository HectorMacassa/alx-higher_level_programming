#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in matrix:
        squared_matrix.append([j**2 for j in i])
    return squared_matrix
