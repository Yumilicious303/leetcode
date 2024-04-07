from collections import defaultdict
import heapq
res = 0
def networkDelayTime(times, n, k):
    visited = set()
    adj = defaultdict(list)
    for source, target, time in times:
        adj[source].append([target, time])
    
    heap = [(0, k)]
    while heap:
        cur_time, cur_node = heapq.heappop(heap)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        res = cur_time
        for adj_node, adj_time in adj[cur_node]:
            heapq.heappush(heap, (cur_time + adj_time, adj_node))
    return res if len(visited) == n else -1






print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(networkDelayTime([[1,2,1]], 2, 1))
print(networkDelayTime([[1,2,1]], 2, 2))