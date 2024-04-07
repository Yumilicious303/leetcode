def findCheapestPrice(n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0

    for i in range(k + 1):
        temp = prices.copy()
        for source, destination, price in flights:
            if prices[source] == float('inf'):
                continue
            temp[destination] = min(temp[destination], prices[source] + price)
        prices = temp

    return prices[dst] if prices[dst] != float('inf') else -1







print(findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))