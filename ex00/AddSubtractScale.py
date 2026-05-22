
class Vector:
    def __init__(self, data):
        self.data = list(data)

    def add(self, v):
        for i in range(len(self.data)):
            self.data[i] += v.data[i]

    def sub(self, v):
        for i in range(len(self.data)):
            self.data[i] -= v.data[i]

    def scl(self, a):
        for i in range(len(self.data)):
            self.data[i] *= a
    
    def __add__(self, other):
        return Vector([
            self.data[i] + other.data[i]
            for i in range(len(self.data))
        ])

    def __mul__(self, scalar):
        return Vector([
            x * scalar
            for x in self.data
        ])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
            

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

    
    def __add__(self, other):
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __sub__(self, other):
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __mul__(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)



if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    v1.add(v2)
    print(v1.data)  # Output: [5, 7, 9]

    v1.sub(v2)
    print(v1.data)  # Output: [1, 2, 3]

    v1.scl(2)
    print(v1.data)  # Output: [2, 4, 6]

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    m1.add(m2)
    print(m1.data)  # Output: [[6, 8], [10, 12]]

    m1.sub(m2)
    print(m1.data)  # Output: [[1, 2], [3, 4]]

    m1.scl(0.5)
    print(m1.data)  # Output: [[0.5, 1], [1.5, 2]]