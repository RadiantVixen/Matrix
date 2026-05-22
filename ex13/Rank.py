import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex12.Inverse import Matrix

class Matrix(Matrix):

    def rank(self):
        if not self.data:
            return 0

        rref = self.row_echelon()
        
        eps = 1e-9
        nonzero_rows = 0
        for r in rref.data:
            if any(abs(x) > eps for x in r):
                nonzero_rows += 1

        return nonzero_rows

    Matrix.rank = rank



if __name__ == "__main__":

    u = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    print(u.rank())
    # 3

    u = Matrix([
        [1.0, 2.0, 0.0, 0.0],
        [2.0, 4.0, 0.0, 0.0],
        [-1.0, 2.0, 1.0, 1.0],
    ])
    print(u.rank())
    # 2

    u = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
        [21.0, 18.0, 7.0],
    ])
    print(u.rank())
    # 3
