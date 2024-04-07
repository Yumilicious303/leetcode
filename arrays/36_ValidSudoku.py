#Valid Sudoku
from collections import defaultdict

def isValidSudoku(board):
    inGroup = set()
    rows, cols = 9, 9
    #check rows
    for row in range(rows):
        inGroup.clear()
        for number in board[row]:
            if number != '.':
                if number in inGroup:
                    return False
                else:
                    inGroup.add(number)
    #check cols
    for col in range(cols):
        inGroup.clear()
        for row in range(rows):
            number = board[row][col]
            if number != '.':
                if number in inGroup:
                    return False
                else:
                    inGroup.add(number)
    #check 3x3 boxes
    boxRows, boxCols = 3, 3
    for boxrow in range(boxRows):
        for boxcol in range(boxCols):
            inGroup.clear()
            for r in range(boxrow * 3, (boxrow * 3) + 3):
                for c in range(boxcol * 3, (boxcol * 3) + 3):
                    number = board[r][c]
                    if number != '.':
                        if number in inGroup:
                            return False
                        else:
                            inGroup.add(number)
    return True

def isValidSudokuNeet(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set) # key = (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3 , c // 3)].add(board[r][c])
    return True


board1 = [
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board2 = [
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
board3 = [
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["1",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


print(isValidSudokuNeet(board1))
print(isValidSudokuNeet(board2))
