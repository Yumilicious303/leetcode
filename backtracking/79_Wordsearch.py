#Word Search
def existNeet(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def backtrack(r, c, letter):
        if letter == len(word):
            return True
        if (r < 0 or 
            c < 0 or
            r >= ROWS or
            c >= COLS or
            board[r][c] != word[letter] or 
            (r,c) in path):
                return False
        
        path.add((r,c))
        result = (backtrack(r + 1, c, letter + 1) or 
                  backtrack(r - 1, c, letter + 1) or 
                  backtrack(r, c - 1, letter + 1) or 
                  backtrack(r, c + 1, letter + 1))
        path.remove((r,c))
        return result
    
    for row in range(ROWS):
         for column in range(COLS):
              if backtrack(row, column, 0): return True
    
    return False


def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if (r,c) in visited or board[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True
        
        
        visited.add((r,c))
        if r + 1 < rows: 
            if dfs(r + 1, c, i + 1): return True
        if r - 1 >= 0: 
            if dfs(r - 1, c, i + 1): return True
        if c + 1 < cols: 
            if dfs(r, c + 1, i + 1): return True
        if c - 1 >= 0: 
            if dfs(r, c - 1, i + 1): return True
        visited.remove((r,c))

    for r in range(rows):
        for c in range(cols):
            visited = set()
            if dfs(r, c, 0): return True
    return False                









print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))