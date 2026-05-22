

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ex00.AddSubtractScale import Vector, Matrix


def lerp(u, v, t):
    return (1 - t) * u + t * v

if __name__ == "__main__":

    print(lerp(0., 1., 0.))
    # 0.0

    print(lerp(0., 1., 1.))
    # 1.0

    print(lerp(0., 1., 0.5))
    # 0.5

    print(lerp(21., 42., 0.3))
    # 27.3

    u = Vector([2., 1.])
    v = Vector([4., 2.])

    result = lerp(u, v, 0.3)
    print(result.data)
    # [2.6, 1.3]

    m1 = Matrix([
        [2., 1.],
        [3., 4.]
    ])

    m2 = Matrix([
        [20., 10.],
        [30., 40.]
    ])

    result = lerp(m1, m2, 0.5)

    for row in result.data:
        print(row)

    # [11.0, 5.5]
    # [16.5, 22.0]
    