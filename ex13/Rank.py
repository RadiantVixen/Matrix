import sys
import os
import importlib

sys.path.append(os.path.join(os.path.dirname(__file__), '../ex10'))
row_echelon_form = importlib.import_module("row-echelon-form")
Matrix = row_echelon_form.Matrix

def rank(self):
    if not self.data:
        return 0

    rref = Matrix.row_echelon(self.data)
    
    eps = 1e-9
    nonzero_rows = 0
    for r in rref:
        if any(abs(x) > eps for x in r):
            nonzero_rows += 1

    return nonzero_rows

Matrix.rank = rank

if __name__ == "__main__":
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u.rank())  # 3

    u = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],
        [-1., 2., 1., 1.],
    ])
    print(u.rank())  # 2

    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.],
    ])
    print(u.rank())  # 3
