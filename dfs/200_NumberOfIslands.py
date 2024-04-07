#Number of Islands
def numIslands(grid):
    land = set()
    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            #print(r, c)
            if grid[r][c] == '1':
                if ((r + 1, c) not in land and
                    (r-1, c) not in land and
                    (r, c - 1) not in land and
                    (r, c + 1) not in land):
                        if (r - 1, c + 1) in land and c < len(grid[0]) - 1 and grid[r][c+1] == '1':
                             pass
                        else:
                             islands = islands + 1
                land.add((r,c))
    return islands

def numIslands2(grid):
    land = set()
    islands = 0

    def dfs(r,c):
        if grid[r][c] == '0':
            return
        if (r,c) not in land:
            land.add((r,c))
        else:
             return
        #dfs up
        if r > 0:
            dfs(r - 1, c)
        #dfs down
        if r < len(grid) - 1:
            dfs(r + 1, c)
        #dfs left
        if c > 0:
            dfs(r, c - 1)
        #dfs right
        if c < len(grid[0]) - 1:
            dfs(r, c + 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                 if (r,c) not in land:
                        islands = islands + 1
                 dfs(r,c)
                 
    return islands

def numIslands3(grid):
    islands = 0

    def dfs(r,c):
        if grid[r][c] == '0' or grid[r][c] == '2':
            return
        if grid[r][c] == '1':
            grid[r][c] = '2' #replace 1 with 2 to signify that we've already come across this land and not count it as a separate island
        #dfs up
        if r > 0:
            dfs(r - 1, c)
        #dfs down
        if r < len(grid) - 1:
            dfs(r + 1, c)
        #dfs left
        if c > 0:
            dfs(r, c - 1)
        #dfs right
        if c < len(grid[0]) - 1:
            dfs(r, c + 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                islands = islands + 1
                dfs(r,c)
                 
    return islands



        


         


grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid3 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]]

grid4 = [
     ["1","0","1","1","1"],
     ["1","0","1","0","1"],
     ["1","1","1","0","1"]]

#print(numIslands(grid))
#print(numIslands(grid2))
#print(numIslands(grid3))


print(numIslands3(grid1))
print(numIslands3(grid2))
print(numIslands3(grid3))
print(numIslands3(grid4))