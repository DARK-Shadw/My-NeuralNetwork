import random

class Matrix:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.matrix = []

        for row in range(self.row):
            c_row = []
            for col in range(self.col):
                c_row.append(0)
            self.matrix.append(c_row)


    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.matrix[i][0] = arr[i]

        return m
    

    def toArray(self):
        out = []
        for i in range(self.row):
            for j in range(self.col):
                out.append(self.matrix[i][j])
        return out

        

    def randomize(self):
        for row in range(self.row):
            for col in range(self.col):
                self.matrix[row][col] = random.uniform(-1, 1)


    def add(self, n):
        if isinstance(n, Matrix):
            for row in range(self.row):
                for col in range(self.col):
                    self.matrix[row][col] = self.matrix[row][col] + n.matrix[row][col]

        else:
            for row in range(self.row):
                for col in range(self.col):
                    self.matrix[row][col] = self.matrix[row][col] + n

    @staticmethod
    def substract(a, b):
        m = Matrix(a.row, a.col)
        for row in range(a.row):
                    for col in range(a.col):
                        m.matrix[row][col] = a.matrix[row][col] - b.matrix[row][col]

        return m


    @staticmethod
    def multiply(a, b):
        result = Matrix(a.row, b.col)
        for i in range(result.row):
            for j in range(result.col):
                sum = 0
                for k in range(a.col):
                    sum += a.matrix[i][k] * b.matrix[k][j]
                result.matrix[i][j] = sum
        return result


    def multiply_scalar(self, n):
        for row in range(self.row):
            for col in range(self.col):
                self.matrix[row][col] = self.matrix[row][col] * n

    @staticmethod
    def transpose(input):
        result = Matrix(input.col, input.row)
        for row in range(input.row):
                for col in range(input.col):
                    result.matrix[col][row] = input.matrix[row][col]

        return result

    def printMatrix(self):
        print(self.matrix)

    def map(self, fn):
        for row in range(self.row):
                for col in range(self.col):
                    val = self.matrix[row][col]
                    self.matrix[row][col] = fn(val)

    @staticmethod
    def static_map(input, fn):
        result = Matrix(input.row, input.col)
        for row in range(input.row):
                for col in range(input.col):
                    val = input.matrix[row][col]
                    result.matrix[row][col] = fn(val)
        return result
        
