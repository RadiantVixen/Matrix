

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ex00.AddSubtractScale import Vector


def linear_combination(vectors, coefs):
    if len(vectors) != len(coefs):
        raise ValueError("vectors and coefficients must have same length")

    size = len(vectors[0].data)

    for v in vectors:
        if len(v.data) != size:
            raise ValueError("all vectors must have same dimension")

    result = [0.0] * size

    for i in range(len(vectors)):
        for j in range(size):
            result[j] += vectors[i].data[j] * coefs[i]

    return Vector(result)

if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([7, 8, 9])

    coefs = [0.5, 1.5, -1]

    result = linear_combination([v1, v2, v3], coefs)

    print(result.data)  # Output: [0.5*1 + 1.5*4 + (-1)*7, 0.5*2 + 1.5*5 + (-1)*8, 0.5*3 + 1.5*6 + (-1)*9]


