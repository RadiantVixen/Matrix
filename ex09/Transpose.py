import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex08.Trace import Matrix


class Matrix(Matrix):
    def transpose(self):
        if not self.data or not self.data[0]:
            return Matrix([])
        
        rows = len(self.data)
        cols = len(self.data[0])
        
        transposed = [[0.0] * rows for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = self.data[i][j]
        
        return Matrix(transposed)

if __name__ == "__main__":
    u = Matrix([
        [1., 2., 3.],
        [4., 5., 6.]
    ])
    print(u.transpose().data)
    # [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(u.transpose().data)
    # [[1.0, 0.0], [0.0, 1.0]]

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.]
    ])
    print(u.transpose().data)
    # [[2.0, 4.0, -2.0], [-5.0, 3.0, 3.0], [0.0, 7.0, 4.0]]
    