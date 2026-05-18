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
    
    def mul_vec(self, v):
        if len(self.data[0]) != len(v.data):
            raise ValueError("Matrix column count must match vector size.")

        result_data = [0] * len(self.data)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result_data[i] += self.data[i][j] * v.data[j]

        return Vector(result_data)
    def mul_mat(self, m):
        if len(self.data[0]) != len(m.data):
            raise ValueError("Matrix A column count must match Matrix B row count.")

        result_data = [[0] * len(m.data[0]) for _ in range(len(self.data))]

        for i in range(len(self.data)):
            for j in range(len(m.data[0])):
                for k in range(len(self.data[0])):
                    result_data[i][j] += self.data[i][k] * m.data[k][j]

        return Matrix(result_data)


if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    result_mat = m1.mul_mat(m2)
    print(result_mat.data)  # Output: [[19, 22], [43, 50]]

    v = Vector([1, 2])
    result_vec = m1.mul_vec(v)
    print(result_vec.data)  # Output: [5, 11]