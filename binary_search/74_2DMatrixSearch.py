#Search 2D Matrix
def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1
    left, right = 0, COLS - 1

    while top <= bottom:
        row = (bottom + top) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    if top > bottom:
        return False
    
    while left <= right:
        col = (left + right) // 2
        if target > matrix[row][col]:
            left = col + 1
        elif target < matrix[row][col]:
            right = col - 1
        else:
            return True
    
    return False
    
#O(log(m * n)



x = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
y = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(searchMatrix(x, 3))
print(searchMatrix(x, 13))
print(searchMatrix(y, 5))
