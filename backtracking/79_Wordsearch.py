#Word Search
def exist(board, word):
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


                









print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))