def rotate(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for r in range(rows):
        for c in range(r, cols):
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp
    for r in matrix:
        r.reverse()
    return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))