import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex04.Norm import Vector
from ex11.determinant import Matrix

class Matrix(Matrix):

    def inverse(matrix):

        rows = len(matrix.data)
        cols = len(matrix.data[0])

        m = [row[:] for row in matrix.data]

        I = [[1 if i == j else 0 for j in range(rows)]
            for i in range(rows)]

        pivot_row = 0

        for col in range(cols):

            if pivot_row >= rows:
                break

            pivot = pivot_row

            while pivot < rows and m[pivot][col] == 0:
                pivot += 1

            if pivot == rows:
                continue

            m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
            I[pivot_row], I[pivot] = I[pivot], I[pivot_row]

            pivot_value = m[pivot_row][col]

            for j in range(cols):
                m[pivot_row][j] /= pivot_value
                I[pivot_row][j] /= pivot_value

            for i in range(rows):

                if i != pivot_row:

                    factor = m[i][col]

                    for j in range(cols):
                        m[i][j] -= factor * m[pivot_row][j]
                        I[i][j] -= factor * I[pivot_row][j]

            pivot_row += 1

        return I


if __name__ == "__main__":

    u = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    print(u.inverse())
    # [[1.0, 0.0, 0.0],
    #  [0.0, 1.0, 0.0],
    #  [0.0, 0.0, 1.0]]

    u = Matrix([
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    print(u.inverse())
    # [[0.5, 0.0, 0.0],
    #  [0.0, 0.5, 0.0],
    #  [0.0, 0.0, 0.5]]

    u = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
    ])
    print(u.inverse())
    # [[0.649425287, 0.097701149, -0.655172414],
    #  [-0.781609195, -0.126436782, 0.965517241],
    #  [0.143678161, 0.074712644, -0.206896552]]