#Min Cost Connect Points
import heapq
def minCostConnectPoints(points):
    visited = set()
    heap = [(0, points[0][0], points[0][1])]
    heapq.heapify(heap)
    res = 0

    while len(visited) < len(points):
        mincost, cur_x, cur_y = heapq.heappop(heap)
        if (cur_x, cur_y) in visited:
            continue
        res += mincost
        visited.add((cur_x, cur_y))
        for x, y in points:
            if (x, y) not in visited:
                manhatten_distance = abs(x - cur_x) + abs(y - cur_y)
                heapq.heappush(heap, (manhatten_distance, x, y))
    return res


def minCostConnectPoints(points):
    N = len(points)
    adj = {i: [] for i in range(N)}  # i : list of [cost, node]
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's
    res = 0
    visit = set()
    minH = [[0, 0]]  # [cost, point]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
    return res



print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(minCostConnectPoints([[3,12],[-2,5],[-4,1]]))