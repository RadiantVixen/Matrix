
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex10.RowEchelonForm import Matrix

class Matrix(Matrix):
    def determinant(matrix):
        m = [row[:] for row in matrix.data]

        n = len(m)
        swaps = 0


        for col in range(n):

            pivot = col

            while pivot < n and m[pivot][col] == 0:
                pivot += 1

            if pivot == n:
                return 0

            if pivot != col:
                m[col], m[pivot] = m[pivot], m[col]
                swaps += 1

            for row in range(col + 1, n):

                factor = m[row][col] / m[col][col]

                for j in range(col, n):
                    m[row][j] -= factor * m[col][j]

        det = 1

        for i in range(n):
            det *= m[i][i]

        if swaps % 2 == 1:
            det *= -1

        return det



if __name__ == "__main__":

    u = Matrix([
        [1.0, -1.0],
        [-1.0, 1.0],
    ])
    print(u.determinant())
    # 0.0

    u = Matrix([
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    print(u.determinant())
    # 8.0

    u = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
    ])
    print(u.determinant())
    # -174.0

    u = Matrix([
        [8.0, 5.0, -2.0, 4.0],
        [4.0, 2.5, 20.0, 4.0],
        [8.0, 5.0, 1.0, 4.0],
        [28.0, -4.0, 17.0, 1.0],
    ])
    print(u.determinant())
    # 1032.0

