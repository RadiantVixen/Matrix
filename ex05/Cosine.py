


import math


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

    def norm_1(self):
        s = 0

        for x in self.data:
            s += abs(x)

        return s
    
    def norm(self):
        s = 0

        for x in self.data:
            s += x * x

        return math.sqrt(s)

    def norm_inf(self):
        m = 0

        for x in self.data:
            m = max(m, abs(x))

        return m
 
def angle_cos(u, v):
    return u.dot(v) / (u.norm() * v.norm())

if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    result = angle_cos(v1, v2)