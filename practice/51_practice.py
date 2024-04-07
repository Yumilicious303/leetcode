def solveQueens(n):
    board = [['.'] * n for i in range(n)]
    col = set()
    negDiag = set()
    posDiag = set()
    res = []

    def dfs(row):
        if row >= n:
            copy = board.copy()
            for i in range(n):
                copy[i] = ''.join(copy[i])
            res.append(copy)
            return

        
        for c in range(n):
            if (c not in col and
                c - row not in negDiag and
                c + row not in posDiag):

                board[row][c] = 'Q'
                col.add(c)
                negDiag.add(c - row)
                posDiag.add(c + row)
                dfs(row + 1)

                board[row][c] = '.'
                col.remove(c)
                negDiag.remove(c - row)
                posDiag.remove(c + row)
    
    dfs(0)
    return res







print(solveQueens(4))