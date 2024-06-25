#Spiral Matrix
def spiralOrder(matrix):
    res = []
    rows, cols = len(matrix), len(matrix[0])
    left, top = 0, 0
    bottom, right = rows, cols
    while len(res) < rows * cols:
        #right
        for col in range(left, right):
            res.append(matrix[top][col])
        top += 1
        #down
        for row in range(top, bottom):
            res.append(matrix[row][right - 1])
        right -= 1
        #Edge Case: We only have one row or or one column
        if len(res) == rows * cols:
            break
        #left
        for col in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][col])
        bottom -= 1
        #up
        for row in range(bottom - 1, top - 1, -1):
            res.append(matrix[row][left])
        left += 1
    
    return res
#print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
