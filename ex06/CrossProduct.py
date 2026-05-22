
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ex04.Norm import Vector


def cross_product(u, v):
    if len(u.data) != 3 or len(v.data) != 3:
        raise ValueError("Both vectors must be 3-dimensional.")

    u_x, u_y, u_z = u.data
    v_x, v_y, v_z = v.data

    cross_prod_data = [
        u_y * v_z - u_z * v_y,
        u_z * v_x - u_x * v_z,
        u_x * v_y - u_y * v_x
    ]

    return Vector(cross_prod_data)



if __name__ == "__main__":
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(cross_product(u, v).data)
    # [0.0, 1.0, 0.0]

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(cross_product(u, v).data)
    # [-3.0, 6.0, -3.0]

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(cross_product(u, v).data)
    # [17.0, -58.0, -16.0]