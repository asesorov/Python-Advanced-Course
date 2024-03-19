import numpy as np

import hashlib
from pathlib import Path


ARTIFACTS_PATH = Path(__file__).resolve().parents[1] / 'artifacts' / '3.3'
np.random.seed(0)


def matrix_hash(matrix):
    """
    Простейшая хэш-функция - сумма элементов матрицы
    """
    return sum(matrix.flat)


class HashMixin:
    def __hash__(self):
        sum = 0
        for i in range(self.rows):
            for j in range(self.cols):
                sum += self.matrix[i][j]
        return sum


class Matrix(HashMixin):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.cache = {}

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            result.append(row)
        
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for component-wise multiplication")
        
        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)]
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other, use_cache=True):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")

        key = hash(other)
        if use_cache and key in self.cache:
            return self.cache[key]
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        product = Matrix(result)
        if use_cache:
            self.cache[key] = product
        return product

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


def create_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix_data = eval(file.read())
        return Matrix(matrix_data)


def main():
    A = create_matrix_from_file(f'{ARTIFACTS_PATH}/A.txt')
    B = create_matrix_from_file(f'{ARTIFACTS_PATH}/B.txt')
    C = create_matrix_from_file(f'{ARTIFACTS_PATH}/C.txt')
    D = create_matrix_from_file(f'{ARTIFACTS_PATH}/D.txt')

    AB = A @ B
    CD = C.__matmul__(D, use_cache=False)
    
    with open(f'{ARTIFACTS_PATH}/AB.txt', 'w') as f:
        f.write(str(AB))
    
    with open(f'{ARTIFACTS_PATH}/CD.txt', 'w') as f:
        f.write(str(CD))
    
    with open(f'{ARTIFACTS_PATH}/hash.txt', 'w') as f:
        f.write(f"Hash AB: {hash(AB)}\nHash CD: {hash(CD)}")

if __name__ == '__main__':
    main()
