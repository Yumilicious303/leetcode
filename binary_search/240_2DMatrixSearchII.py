#2D Matrix Search II

#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.

def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    row, col = ROWS - 1, 0

    while row >= 0 and col < COLS:
        print(matrix[row][col])
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    
    return False
            
        



x = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

print(searchMatrix(x, 5))
print(searchMatrix(x, 20))