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


    for r in range(rows):
        for c in range(cols):
            visited = set()
            if dfs(r, c, 0): return True
    return False

#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
#print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
#print(exist(['a'], 'a'))
print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))