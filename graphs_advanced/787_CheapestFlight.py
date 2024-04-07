#Cheapest Flight
from collections import defaultdict
import heapq
def findCheapestPrice(n, flights, src, dst, k):
    res = 0
    adj = defaultdict(list)
    visited = defaultdict(lambda: 0)
    heap = [(0, src, k + 1)]
    for where_from, where_to, price in flights:
        adj[where_from].append((where_to, price))

    while heap:
        cur_price, cur_airport, cur_k = heapq.heappop(heap)
        if cur_airport == dst:
            return cur_price 
        if visited[cur_airport] >= cur_k:
              continue
        visited[cur_airport] = cur_k

        
        for destination, price in adj[cur_airport]:
            heapq.heappush(heap, (cur_price + price, destination, cur_k - 1))
    return -1

def findCheapestPriceLeet(n, flights, src, dst, k):
	graph = defaultdict(dict)
	for s, d, w in flights:
		graph[s][d] = w
	pq = [(0, src, k+1)]
	vis = [0] * n
	while pq:
		w, x, k = heapq.heappop(pq)
		if x == dst:
			return w
		if vis[x] >= k:
			continue
		vis[x] = k
		for y, dw in graph[x].items():
			heapq.heappush(pq, (w+dw, y, k-1))
	return -1

def findCheapestPriceNeet(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0
    print(prices)
    for i in range(k + 1):
        tmpPrices = prices.copy()
        for s, d, p in flights:  # s=source, d=dest, p=price
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices
        print(prices)
    return -1 if prices[dst] == float("inf") else prices[dst]






#print(findCheapestPriceNeet(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
#print(findCheapestPriceNeet(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
#print(findCheapestPriceNeet(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))
print(findCheapestPriceNeet(n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1))
#print(findCheapestPriceNeet(n = 13, flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]], src = 10, dst = 1, k = 10))