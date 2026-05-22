import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex00.AddSubtractScale import Matrix


class Matrix(Matrix):
    
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
    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v).data)
    # [4.0, 2.0]

    u = Matrix([
        [2., 0.],
        [0., 2.]
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v).data)
    # [8.0, 4.0]

    u = Matrix([
        [2., -2.],
        [-2., 2.]
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v).data)
    # [4.0, -4.0]

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    v = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(u.mul_mat(v).data)
    # [[1.0, 0.0], [0.0, 1.0]]

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(u.mul_mat(v).data)
    # [[2.0, 1.0], [4.0, 2.0]]

    u = Matrix([
        [3., -5.],
        [6., 8.]
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(u.mul_mat(v).data)
    # [[-14.0, -7.0], [44.0, 22.0]]