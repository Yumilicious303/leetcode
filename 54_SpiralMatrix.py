#Spiral Matrix
def spiralOrder(matrix):
    left, right =  0, len(matrix[0])
    top, bottom = 0, len(matrix)
    output = []

    mSize = len(matrix) * len(matrix[0])
    currsize = 0

    while currsize < mSize:
        #move right
        for i in range(left,right):
            output.append(matrix[top][i])
            currsize += 1
        top = top + 1
        #move down
        for i in range(top, bottom):
            output.append(matrix[i][right - 1])
            currsize += 1
        right = right - 1
        #move left
        for i in range(right - 1,left - 1, -1):
            output.append(matrix[bottom - 1][i])
            currsize += 1
        bottom = bottom - 1
        #move up
        for i in range(bottom - 1, top - 1, -1):
            output.append(matrix[i][left])
            currsize += 1
        left = left + 1
    return output





print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
