#Task Scheduler
import heapq
from collections import Counter, deque
def leastInterval(tasks, n): #probably study this one
    time = 0
    count = Counter(tasks)
    q = deque()

    heap = [-i for i in count.values()]
    heapq.heapify(heap)

    while heap or q:
        if q and time > q[0][1]:
                task, cooldown_end = q.popleft()
                heapq.heappush(heap, task)
        if heap:
            task = heapq.heappop(heap)
            task += 1
            if task < 0:
                q.append([task, time + n])
        time += 1
    return time

def leastIntervalNeet(tasks, n):
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)
    
    time = 0
    q = deque()
    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
  
    return time



print(leastInterval(["A","A","A","B","B","B"], 2))
print(leastInterval(["A","C","A","B","D","B"], 1))
print(leastInterval(["A","A","A","B","B","B"], 3))
    
