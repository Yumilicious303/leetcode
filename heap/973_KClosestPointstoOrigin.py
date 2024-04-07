#K Closest Points to Origin
import math
import heapq

def kClosest(points, k):
    res = []
    heap = [[math.sqrt(x**2 + y**2), x, y] for x, y in points]
    heapq.heapify(heap)
    for i in range(k):
        dist, x, y = heapq.heappop(heap)
        res.append([x, y])
    return res



print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))