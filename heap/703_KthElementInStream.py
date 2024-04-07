#Kth Element in Stream
import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    def add(self, val):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

    
k = KthLargest(3, [4, 5, 8, 2])
print(k.add(3))
print(k.add(5))
print(k.add(10))
print(k.add(9))
print(k.add(4))