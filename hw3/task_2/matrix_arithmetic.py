import numpy as np

from pathlib import Path


ARTIFACTS_PATH = Path(__file__).resolve().parents[1] / 'artifacts' / '3.2'
np.random.seed(0)


class MatrixOperations:
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            result.append(row)
        
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        
        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
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

    def __truediv__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for division")
        
        result = []
        for i in range(self.rows):
            row = [self.matrix[i][j] / other.matrix[i][j] for j in range(self.cols)]
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")

        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)


class MatrixIO:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.matrix:
                f.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        return np.array2string(self.matrix)


class Matrix(MatrixOperations, MatrixIO):
    def __init__(self, matrix):
        self._matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = np.array(value)

def main():
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix_sum = matrix1 + matrix2
    matrix_hadamard_product = matrix1 * matrix2
    matrix_product = matrix1 @ matrix2

    matrix_sum.save_to_file(f'{ARTIFACTS_PATH}/matrix+.txt')
    matrix_hadamard_product.save_to_file(f'{ARTIFACTS_PATH}/matrix*.txt')
    matrix_product.save_to_file(f'{ARTIFACTS_PATH}/matrix@.txt')


if __name__ == '__main__':
    main()
