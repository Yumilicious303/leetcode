#Hand of Straights
import heapq
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    count = {}
    for h in hand:
        count[h] = count.get(h, 0) + 1
    heap = list(count.keys())
    heapq.heapify(heap)

    curr_hand = 0
    prev = None
    while heap:
        if prev is not None:
            value = prev + 1
        else:
            value = heap[0]
        
        if value not in count or count[value] == 0:
            return False
        else:
            count[value] -= 1
            if count[value] == 0:
                if value == heap[0]:
                    heapq.heappop(heap)
                else:
                    return False
            
        curr_hand += 1
        prev = value
        if curr_hand == groupSize:
            prev = None
            curr_hand = 0
    return True

def isNStraightHandNeet(hand, groupSize):
    if len(hand) % groupSize:
        return False
    
    count = {}
    for n in hand:
        count[n] = count.get(n, 0) + 1
        
    minH = list(count.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]

        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count -= 1
            if count [i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)
    return True




print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(isNStraightHand([1,2,3,6,2,3,4,7,9], 3))
print(isNStraightHand([0,0], 2))