import numpy as np

def input_matrix(rows, cols):
    print(f"Enter the elements of a {rows}x{cols} matrix, separated by spaces:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def matrix_addition(matrix_a, matrix_b):
    return np.add(matrix_a, matrix_b)

def matrix_subtraction(matrix_a, matrix_b):
    return np.subtract(matrix_a, matrix_b)

def matrix_multiplication(matrix_a, matrix_b):
    return np.matmul(matrix_a, matrix_b)

def matrix_division(matrix_a, matrix_b):
    return np.matmul(matrix_a, np.linalg.inv(matrix_b))

def matrix_determinant(matrix):
    return np.linalg.det(matrix)

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)
