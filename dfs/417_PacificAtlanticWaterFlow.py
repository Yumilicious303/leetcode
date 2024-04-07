#Pacific Atlanctic WaterFlow
def pacificAtlantic(heights):
    def dfs(r, c, visited):
        if r == 1 and c == 4:
            pass
        if (r, c) in finalOcean:
            return finalOcean[(r, c)]
        if (r, c) in visited:
            return
        if (r == rows - 1 and c == 0) or (c == cols - 1 and r == 0):
            finalOcean[(r, c)] = 'PA'
            res.append([r, c])
            return 'PA'
        visited.add((r,c))
        
        
        flows = set()
        #up
        if r > 0 and heights[r - 1][c] <= heights[r][c]:
            flows.add(dfs(r - 1, c, visited))
        #down
        if r < rows - 1 and heights[r + 1][c] <= heights[r][c]:
            flows.add(dfs(r + 1, c, visited))
        #left
        if c > 0 and heights[r][c - 1] <= heights[r][c]:
            flows.add(dfs(r, c - 1, visited))
        #right
        if c < cols - 1 and heights[r][c + 1] <= heights[r][c]:    
            flows.add(dfs(r, c + 1, visited))
        
        if 'PA' in flows or ('P' in flows and 'A' in flows):
            finalOcean[(r, c)] = 'PA'
            res.append([r, c])
            return 'PA'
        if 'P' in flows or r == 0 or c == 0:
            finalOcean[(r, c)] = 'P'
            return 'P'
        if 'A' in flows or r == rows - 1 or c == cols - 1:
            finalOcean[(r, c)] = 'A'
            return 'A'

        finalOcean[(r, c)] = None
        return None
        
    res = []
    rows, cols = len(heights), len(heights[0])
    finalOcean = {}
    for r in range(rows):
        for c in range(cols):
            dfs(r,c, set())
    return res

def pacificAtlanticNeet(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    def dfs(r, c, visit, prevHeight):
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prevHeight
        ):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res

def pacificAtlantic2(heights):
    def dfs(r, c, visited, previousHeight):
        if ((r, c) in visited or
            r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            heights[r][c] < previousHeight
            ):
            return
        visited.add((r,c))

        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    rows, cols = len(heights), len(heights[0])
    atlantic, pacific = set(), set()

    for r in range(rows):
        dfs(r, 0, pacific, 0)
        dfs(r, cols - 1, atlantic, 0)
    
    for c in range(cols):
        dfs(0, c, pacific, 0)
        dfs(rows - 1, c, atlantic, 0)

    return [list(x) for x in pacific.intersection(atlantic)]




heights1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlanticNeet(heights1))