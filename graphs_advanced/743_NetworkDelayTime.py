#Network Delay Time
from collections import defaultdict
import heapq
def networkDelayTime(times, n, k):
    edges = defaultdict(list)
    for source, target, time in times:
        edges[source].append((target, time))

    minHeap = [(0, k)]
    visit = set()
    res = 0
    while minHeap:
        time_cur, node_cur = heapq.heappop(minHeap)
        if node_cur in visit:
            continue
        visit.add(node_cur)
        res = time_cur

        for node_adj, time_adj in edges[node_cur]:
            if node_adj not in visit:
                heapq.heappush(minHeap, (time_cur + time_adj, node_adj))
    return res if len(visit) == n else -1

#E = V^2
# O(E * logV)

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))