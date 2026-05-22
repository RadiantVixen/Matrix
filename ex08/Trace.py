import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex07.LinearMap import Matrix


class Matrix(Matrix):
    
    def trace(self):
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix must be square to compute trace.")

        trace_sum = 0
        for i in range(len(self.data)):
            trace_sum += self.data[i][i]

        return trace_sum


if __name__ == "__main__":
    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(u.trace())
    # 2.0

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.]
    ])
    print(u.trace())
    # 9.0

    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.]
    ])
    print(u.trace())
    # -21.0