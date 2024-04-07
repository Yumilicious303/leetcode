#Max Area of Island
def maxAreaofIsland(grid):
    def dfs(r, c):
        if grid[r][c] != 1:
            return 0
        
        grid[r][c] = 2

        up, down, left, right = 0, 0, 0, 0
        #search up
        if r > 0:
            up = dfs(r - 1, c)
        #search down
        if r < rows - 1:
            down = dfs(r + 1, c)
        #search left
        if c > 0:
            left = dfs(r, c - 1)
        #search right
        if c < cols - 1:
            right = dfs(r, c + 1)
        
        
        return 1 + up + down + left + right


    rows, cols = len(grid), len(grid[0])
    res = 0
    for r in range(rows):
        for c in range(cols):
            res = max(res, dfs(r, c))
    return res
    
            



grid1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid2 = [[0,0,0,0,0,0,0,0]]


print(maxAreaofIsland(grid1))
print(maxAreaofIsland(grid2))
