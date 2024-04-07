#Rotate Image
def rotate(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    for row in range(ROWS):
        for col in range(row, COLS):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
        
        for row in matrix:
            row.reverse()




rotate([[1,2,3],[4,5,6],[7,8,9]])