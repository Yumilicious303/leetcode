#Top K Frequent Elements
import heapq
def topKFrequent(nums, k):
    dict = {}
    heap = []
    res = []
    for n in nums:
        dict[n] = dict.get(n, 0) + 1
    for char, count in dict.items():
        heap.append([-count, char])
    heapq.heapify(heap)
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res

def topKFrequentNeet(nums, k):
    count = {}
    res = []
    bucket = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for n, count in count.items():
        bucket[count].append(n)
    
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res
    


    

print(topKFrequentNeet([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))