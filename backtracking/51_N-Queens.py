#N Queens
def solveNQueens(n):
    def dfs(r, c, Q, cols, negDiag, posDiag, cur):
        if (c in cols or 
            r -c in negDiag or
            r + c in posDiag or
            r >= n):
            return
        
        cur[r][c] = 'Q'
        Q += 1

        if Q == n:
            copy = [''.join(row) for row in cur]
            res.append(copy)
        
        cols.add(c)
        negDiag.add(r - c)
        posDiag.add(r + c)

        for c in range(n):
            dfs(r + 1, c, Q, cols, negDiag, posDiag, cur)
    res = []
    for c in range(n):
        dfs(0, c, 0, set(), set(), set(), [['.' for i in range(n)] for j in range(n)])
    return res
    

def solveNQueensNeet(n):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [['.'] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            
            col.add(c)
            posDiag.add((r + c))
            negDiag.add((r - c))
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove((r + c))
            negDiag.remove((r - c))
            board[r][c] = '.'

    backtrack(0)
    return res






print(solveNQueensNeet(4))
