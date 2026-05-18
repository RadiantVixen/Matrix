
def Transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

if __name__ == "__main__":
    m1 = [[1, 2],
         [3, 4]]
    result = Transpose(m1)
    print(result)  # Output: [[1, 3], [2, 4]]
    