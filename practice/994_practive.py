from collections import deque
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    time = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append([r, c])
            if grid[r][c] == 1:
                fresh += 1 
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2 
                q.append([r - 1, c])
                fresh -= 1
            if r + 1 < rows and grid[r + 1][c] == 1: 
                grid[r + 1][c] = 2
                q.append([r + 1, c])
                fresh -= 1
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                q.append([r, c - 1])
                fresh -= 1
            if c + 1 < cols and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                q.append([r, c + 1])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1
        
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))