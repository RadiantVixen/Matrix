
def determinant(matrix):
    m = [row[:] for row in matrix]

    n = len(m)
    swaps = 0


    for col in range(n):

        # Find pivot
        pivot = col

        while pivot < n and m[pivot][col] == 0:
            pivot += 1

        # No pivot => determinant = 0
        if pivot == n:
            return 0

        # Swap rows
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            swaps += 1

        # Eliminate rows below
        for row in range(col + 1, n):

            factor = m[row][col] / m[col][col]

            for j in range(col, n):
                m[row][j] -= factor * m[col][j]

    # Product of diagonal
    det = 1

    for i in range(n):
        det *= m[i][i]

    # Adjust sign
    if swaps % 2 == 1:
        det *= -1

    return det



if __name__ == "__main__":
    m = [[1, 2, 3], [5, 6, 9], [6, 3, 8],]
    m = determinant(m)
    print(m)

