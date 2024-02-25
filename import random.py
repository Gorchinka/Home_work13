import random

def generate_matrix(size):
    matrix = [[random.randint(0, 100) for _ in range(size[1])] for _ in range(size[0])]
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинаковой размерности")
    
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

matrix1 = generate_matrix((10, 10))
matrix2 = generate_matrix((10, 10))
matrix3 = add_matrices(matrix1, matrix2)

print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nМатрица 3 (сложение матриц 1 и 2):")
for row in matrix3:
    print(row)