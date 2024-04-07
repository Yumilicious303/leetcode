#Last Stone Weight
import heapq
def lastStoneWeight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone_one = heapq.heappop(stones)
        stone_two = heapq.heappop(stones)
        if stone_one != stone_two:
            heapq.heappush(stones, (min(stone_two - stone_one, stone_one - stone_two)))
    if stones: return stones[0] * -1
    else: return 0

def lastStoneWeightNeet(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))