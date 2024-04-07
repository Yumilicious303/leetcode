#Walls and Gates
def walls_and_gates(rooms):
    def dfs(r, c, distanceToNearestGate, visited):
        if ((r,c) in visited or
            r >= rows or 
            r < 0 or
            c >= cols or 
            c < 0 or
            rooms[r][c] < 0):
            return
        
        visited.add((r,c))
        rooms[r][c] = min(rooms[r][c], distanceToNearestGate)

        dfs(r + 1, c, distanceToNearestGate + 1, visited)
        dfs(r - 1, c, distanceToNearestGate + 1, visited)
        dfs(r, c + 1, distanceToNearestGate + 1, visited)
        dfs(r, c - 1, distanceToNearestGate + 1, visited)
        
    rows, cols = len(rooms), len(rooms[0])

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                dfs(r, c, 0, set())
    return rooms




rooms1 = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]

print(walls_and_gates(rooms1))