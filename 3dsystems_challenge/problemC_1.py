import heapq
def maxKitties(total_beds, intervals):
    total_kittens = len(intervals)
    intervals.sort()
    print(intervals)
    heap = []
    res = 0

    for start, end in intervals:
        if heap and (heap[0] * -1) <= start:
            heap = []
        if len(heap) < total_beds:
            res += 1
            heapq.heappush(heap, -1 * end)
        else:
            maxend = -1 * heapq.heappop(heap)
            shorter_kitten = min(maxend, end)
            heapq.heappush(heap, -1 * shorter_kitten)
    return res

def maxKitties2(total_beds, intervals):
    intervals.sort()
    heap = [0] * total_beds
    res = 0
    
    for arrival, departure in intervals:
        earliest_availability = heapq.heappop(heap)
        if arrival >= earliest_availability:
            heapq.heappush(heap, departure)
            res += 1
        else:
            heapq.heappush(heap, min(earliest_availability, departure))
    return res

def maxKitties3(total_beds, intervals):
    intervals.sort()
    minHeap = [0] * total_beds
    maxHeap = []
    res = 0
    
    for arrival, departure in intervals:
        earliest_availability = heapq.heappop(minHeap)
        if arrival >= earliest_availability:
            heapq.heappush(minHeap, departure)
            heapq.heappush(-1 * maxHeap, departure)
            res += 1
        elif maxHeap and departure < (-1 * maxHeap[0]):
            lastDeparture = maxHeap.pop()
            minHeap.remove(-1 * lastDeparture)
            heapq.heapify(minHeap)
            heapq.heappush(minHeap, departure)
            heapq.heappush(maxHeap, departure)
        else: 
            heapq.heappush(minHeap, min(earliest_availability, departure))
    return res

def maxKitties4(total_beds, intervals):
    intervals.sort()
    heap = [0] * total_beds
    res = 0
    lastDeparture = 0
    
    for arrival, departure in intervals:
        earliest_availability = heap[0]
        if arrival >= earliest_availability:
            heapq.heappop(heap)
            heapq.heappush(heap, departure)
            res += 1
            lastDeparture = max(departure, lastDeparture)
        else:
            if departure < lastDeparture:
                heap[heap.index(lastDeparture)] = departure
                heapq.heapify(heap)
                lastDeparture = max(heap)
    return res

def maxKittiesMaxHeap(total_beds, intervals):
    intervals.sort()
    heap = [0] * total_beds
    res = 0
    maxHeap = []
    
    for arrival, departure in intervals:
        earliest_availability = heap[0]
        if arrival >= earliest_availability:
            heapq.heappop(heap)
            heapq.heappush(heap, departure)
            res += 1
            heapq.heappush(maxHeap, departure * -1)
        else:
            lastDeparture = -1 * maxHeap[0]
            if departure < lastDeparture:
                heap[heap.index(lastDeparture)] = departure
                heapq.heapify(heap)
                heapq.heappop(maxHeap)
    return res

def maxKitties6(total_beds, intervals):
    intervals.sort()
    heap = [0] * total_beds
    res = 0
    lastDeparture = 0
    removed = set()
    
    for arrival, departure in intervals:
        while heap[0] in removed:
            removed.remove(heap[0])
            heapq.heappop(heap)
        earliest_availability = heap[0]
        if arrival >= earliest_availability:
            heapq.heappop(heap)
            heapq.heappush(heap, departure)
            res += 1
            lastDeparture = max(departure, lastDeparture)
        else:
            if departure < lastDeparture:
                removed.add(lastDeparture)
                heapq.heappush(heap, departure)
                lastDeparture = max(heap)
    return res

def maxKittiesWiki(total_beds, intervals):
    res = 0
    earliest_availability = 0
    intervals.sort(key=lambda x: x[1])
    heap = [[0, 0] for i in range(total_beds)]
    for arrival, departure in intervals:
        latest_availability = -1 * heap[0][0]
        if arrival >= latest_availability:
            heapq.heappop(heap)
            heapq.heappush(heap, [departure, arrival])
            res += 1
        elif arrival >= earliest_availability:
            temp = []
            while heap[0][0] != (-1 * earliest_availability):
                temp.append(heapq.heappop(heap))
            heapq.heappop(heap)
            for t in temp:
                heapq.heappush(heap, t)
            heapq.heappush(heap, [-1 * departure, -1 * arrival])
            earliest_availability = departure
            res += 1
    return res


def maxKitties8(total_beds, intervals):
    intervals.sort(key=lambda x: x[1])
    heap = [0] * total_beds
    res = 0
    
    for arrival, departure in intervals:
        earliest_availability = heap[0]
        if arrival >= earliest_availability:
            heapq.heappop(heap)
            heapq.heappush(heap, departure)
            res += 1
    return res




print(maxKitties4(1, [[1, 2], [2, 3], [2, 3]]), 'answer: 2')
print(maxKitties4(1, [[1, 3], [4, 6], [7, 8], [2, 5]]), 'answer: 3')
print(maxKitties4(2, [[1, 4], [5, 9], [2, 7], [3, 8], [6, 10]]), 'answer: 3')
print(maxKitties4(1, [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10]]), 'answer: 5')
print(maxKitties4(1, [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]), 'answer: 2') 
print(maxKitties4(2, [[1, 4], [3, 6], [2, 5], [5, 8], [7, 10]]), 'answer: 4') 
print(maxKitties4(2, [[1, 3], [1, 3], [1, 3], [6, 9], [6, 9], [6, 9]]), 'answer: 4') 
print(maxKitties4(1, [[1, 7], [1, 3], [2, 4], [3, 5], [5, 7]]), 'answer: 3') 
print(maxKitties4(2, [[1, 7], [1, 3], [2, 4], [3, 5], [5, 7]]), 'answer: 4') 
print(maxKitties4(1, [[1, 30], [5, 10], [15,20]]), 'answer: 2') 
print(maxKitties4(2, [[1, 30], [5, 10], [15,20]]), 'answer: 3') 
print(maxKitties4(2, [(0, 10), (1, 5), (2, 7), (3, 8)]), 'answer: 2') 
print(maxKitties4(1, [[5, 6]]), 'answer: 1') 
print(maxKitties4(2, [[1, 3], [2, 4], [5, 7], [6, 8]]), 'answer: 4') 
print(maxKitties4(1, [[1, 3], [2, 4], [5, 7], [6, 8]]), 'answer: 2') 
print(maxKitties4(2, [(3, 64), (18, 34), (20, 90), (22, 74), (57, 94), (58, 81), (59, 100), (67, 90), (82, 91), (87, 97)]), 'answer: 5') 

















'''
def max_kittens(k, requests):
    # Sort the requests by the departure time in ascending order
    requests.sort(key=lambda x: x[1])
    
    # Initialize a list to keep track of booked beds
    booked_beds = []
    
    # Iterate through each request and allocate beds greedily
    for request in requests:
        # Check if there are available beds for the current request
        if len(booked_beds) < k:
            booked_beds.append(request[1])
        else:
            # If there are no available beds, remove the request with the latest departure time
            max_departure_time = max(booked_beds)
            if request[0] >= max_departure_time:
                booked_beds.remove(max_departure_time)
                booked_beds.append(request[1])
    
    # The number of accommodated kittens is the size of the booked_beds list
    return len(booked_beds)

print(max_kittens(1, [[1, 2], [2, 3], [2, 3]]))
print(max_kittens(1, [[1, 3], [4, 6], [7, 8], [2, 5]]))
print(max_kittens(2, [[1, 4], [5, 9], [2, 7], [3, 8], [6, 10]]))
'''