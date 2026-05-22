import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ex03.DotProduct import Vector

class Vector(Vector):

    def norm_1(self):
        s = 0

        for x in self.data:
            s += abs(x)

        return s
    
    def norm(self):
        s = 0

        for x in self.data:
            s += x ** 2

        return s ** 0.5

    def norm_inf(self):
        m = 0

        for x in self.data:
            m = max(m, abs(x))

        return m
    
if __name__ == "__main__":
    u = Vector([0., 0., 0.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # 0.0, 0.0, 0.0

    u = Vector([1., 2., 3.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # 6.0, 3.7416573867739413, 3.0

    u = Vector([-1., -2.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # 3.0, 2.23606797749979, 2.0

