import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ex04.Norm import Vector
from ex09.Transpose import Matrix

EPSILON = 1e-10

class Matrix(Matrix):
    def row_echelon(self):
        m = [row[:] for row in self.data]
        rows = len(m)
        if rows == 0:
            return Matrix([])
        cols = len(m[0])
        pivot_row = 0

        for col in range(cols):
            if pivot_row >= rows:
                break

            pivot = pivot_row
            while pivot < rows and abs(m[pivot][col]) < EPSILON:
                pivot += 1
            if pivot == rows:
                continue

            m[pivot_row], m[pivot] = m[pivot], m[pivot_row]

            pivot_value = m[pivot_row][col]
            for j in range(cols):
                m[pivot_row][j] /= pivot_value

            for i in range(rows):
                if i != pivot_row:
                    factor = m[i][col]
                    if abs(factor) < EPSILON:
                        continue
                    for j in range(cols):
                        m[i][j] -= factor * m[pivot_row][j]

            for i in range(rows):
                for j in range(cols):
                    if abs(m[i][j]) < EPSILON:
                        m[i][j] = 0.0

            pivot_row += 1

        return Matrix(m)


if __name__ == "__main__":
    u = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])
    print(u.row_echelon().data)
    # [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    u = Matrix([
        [1.0, 2.0],
        [3.0, 4.0]
    ])
    print(u.row_echelon().data)
    # [[1.0, 0.0], [0.0, 1.0]]

    u = Matrix([
        [1.0, 2.0],
        [2.0, 4.0]
    ])
    print(u.row_echelon().data)
    # [[1.0, 2.0], [0.0, 0.0]]

    u = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0,  1.0, 4.0, 17.0]
    ])
    print(u.row_echelon().data)
    # [[1.0, 0.625, 0.0, 0.0, -12.166...], [0.0, 0.0, 1.0, 0.0, -3.666...], [0.0, 0.0, 0.0, 1.0, 29.5]]
    