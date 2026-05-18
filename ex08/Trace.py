from ex00.AddSubtractScale import Vector

class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def add(self, m):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] += m.data[i][j]

    def sub(self, m):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] -= m.data[i][j]

    def scl(self, a):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] *= a
    
    def trace(self):
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix must be square to compute trace.")

        trace_sum = 0
        for i in range(len(self.data)):
            trace_sum += self.data[i][i]

        return trace_sum


if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    print(m1.trace())

    m2 = Matrix([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
    print(m2.trace())