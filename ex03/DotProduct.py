


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


    def dot(self, v):
        result = 0

        for i in range(len(self.data)):
            result += self.data[i] * v.data[i]

        return result

if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    result = v1.dot(v2)
    print(result)  # Output: 32