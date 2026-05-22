

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ex00.AddSubtractScale import Vector

class Vector(Vector):
    
    def dot(self, v):
        result = 0

        for i in range(len(self.data)):
            result += self.data[i] * v.data[i]

        return result

if __name__ == "__main__":
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))
    # 0.0

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))
    # 2.0

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))
    # 9.0