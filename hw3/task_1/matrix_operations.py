import numpy as np

from pathlib import Path


ARTIFACTS_PATH = Path(__file__).resolve().parents[1] / 'artifacts' / '3.1'
np.random.seed(0)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

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

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")

        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


def main():
    np1 = np.random.randint(0, 10, (10, 10))
    np2 = np.random.randint(0, 10, (10, 10))
    matrix1 = Matrix(np1)
    matrix2 = Matrix(np2)
    #print(np1 + np2)
    #print(np1 * np2)
    #print(np1 @ np2)

    try:
        matrix_sum = matrix1 + matrix2
        matrix_hadamard_product = matrix1 * matrix2
        matrix_product = matrix1 @ matrix2

        with open(f'{ARTIFACTS_PATH}/matrix+.txt', 'w') as f:
            f.write(str(matrix_sum))
        
        with open(f'{ARTIFACTS_PATH}/matrix*.txt', 'w') as f:
            f.write(str(matrix_hadamard_product))
            
        with open(f'{ARTIFACTS_PATH}/matrix@.txt', 'w') as f:
            f.write(str(matrix_product))

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
