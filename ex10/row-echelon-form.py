
class Matrix:
    def __init__(self, data):
        self.data = [list(map(float, row)) for row in data]


    def row_echelon(matrix):
        m = [row[:] for row in matrix]

        rows = len(m)
        cols = len(m[0])

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


            pivot_value = m[pivot_row][col]

            for j in range(cols):
                m[pivot_row][j] /= pivot_value


            for i in range(rows):

                if i != pivot_row:

                    factor = m[i][col]

                    for j in range(cols):
                        m[i][j] -= factor * m[pivot_row][j]

            pivot_row += 1

        return m




if __name__ == "__main__":
    m = [[1, 2, 3], [5, 6, 9], [6, 3, 8],]
    m = m.row_echelon()
    print(m)

