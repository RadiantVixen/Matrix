


from ex00.AddSubtractScale import Vector


def lerp(u, v, t):
    return (1 - t) * u + t * v


def lerp_vector(u, v, t):
    result = []

    for i in range(len(u.data)):
        value = (1 - t) * u.data[i] + t * v.data[i]
        result.append(value)

    return Vector(result)

if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    t = 0.5
    result = lerp_vector(v1, v2, t)

    print(result.data)  # Output: [2.5, 3.5, 4.5]