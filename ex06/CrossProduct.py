
from ex00.AddSubtractScale import Vector


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
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    result = cross_product(v1, v2)
    print(result.data)  # Output: [-3, 6, -3]