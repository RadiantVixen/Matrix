

def inverse(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    m = [row[:] for row in matrix]

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
    m = [
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ]
    m = inverse(m)
    print(m)

    m = [
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ]
    
    m = inverse(m)
    print(m)

    m = [
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ]

    m = inverse(m)
    print(m)