import heapq
def minCostConnectPoints(points):
    res = 0
    visited = set()
    heap = [(0, points[0][0], points[0][1])]
    while len(visited) < len(points):
        cost, cur_x, cur_y = heapq.heappop(heap)
        if (cur_x, cur_y) in visited:
            continue
        res += cost
        visited.add((cur_x, cur_y))

        for x, y in points:
            if (x, y) not in visited:
                manhatten = abs(cur_x - x) + abs(cur_y - y)
                heapq.heappush(heap, (manhatten, x, y))
    return res


print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(minCostConnectPoints([[3,12],[-2,5],[-4,1]]))