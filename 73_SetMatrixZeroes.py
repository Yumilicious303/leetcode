#Set Matrix Zeroes
def setZeroes(matrix):
    changed = set()
    for r, row in enumerate(matrix):
        for n, num in enumerate(row):
            if num == 0 and (r,n) not in changed:
                #set row to 0
                for i in range(len(row)):
                    if matrix[r][i] != 0:
                        matrix[r][i] = 0
                        changed.add((r,i))
                #set col to 0
                for j in range(len(matrix)):
                    if matrix[j][n] != 0:
                        matrix[j][n] = 0
                        changed.add((j,n))
    return matrix

def setZeroesNeet(matrix):
    # O(1)
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False
    # determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
           
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroesNeet([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(setZeroesNeet([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))



