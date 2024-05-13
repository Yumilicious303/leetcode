import heapq
def interval_scheduling2(k, intervals):
    res = 0
    intervals.sort(key=lambda x: x[1])
    beds = [0 for i in range(k)]
    
    for arrival, departure in intervals:
        worst_bed = -1
        worst_bed_index = -1
        for bed_index, bed in enumerate(beds):
            if bed > worst_bed and bed <= arrival:
                worst_bed = bed
                worst_bed_index = bed_index
        
        if worst_bed > -1:
            beds[worst_bed_index] = departure
            res += 1

    return res

def interval_scheduling3(k, intervals):
    res = 0
    intervals.sort(key=lambda x: x[1])
    beds = [0 for i in range(k)]

    for arrival, departure in intervals:
        temp = []
        while beds and beds[0] * -1 > arrival:
            t = heapq.heappop(beds)
            temp.append(t)
        if beds:
            heapq.heappop(beds)
            heapq.heappush(beds, -1 * departure)
            res += 1
        for t in temp:
            heapq.heappush(beds, t)
    return res

print(interval_scheduling3(1, [[1, 2], [2, 3], [2, 3]]), 'answer: 2')
print(interval_scheduling3(1, [[1, 3], [4, 6], [7, 8], [2, 5]]), 'answer: 3')
print(interval_scheduling3(2, [[1, 4], [5, 9], [2, 7], [3, 8], [6, 10]]), 'answer: 3')
print(interval_scheduling3(1, [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10]]), 'answer: 5')
print(interval_scheduling3(1, [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]), 'answer: 2') 
print(interval_scheduling3(2, [[1, 4], [3, 6], [2, 5], [5, 8], [7, 10]]), 'answer: 4') 
print(interval_scheduling3(2, [[1, 3], [1, 3], [1, 3], [6, 9], [6, 9], [6, 9]]), 'answer: 4') 
print(interval_scheduling3(1, [[1, 7], [1, 3], [2, 4], [3, 5], [5, 7]]), 'answer: 3') 
print(interval_scheduling3(2, [[1, 7], [1, 3], [2, 4], [3, 5], [5, 7]]), 'answer: 4') 
print(interval_scheduling3(1, [[1, 30], [5, 10], [15,20]]), 'answer: 2') 
print(interval_scheduling3(2, [[1, 30], [5, 10], [15,20]]), 'answer: 3') 
print(interval_scheduling3(2, [(0, 10), (1, 5), (2, 7), (3, 8)]), 'answer: 2') 
print(interval_scheduling3(1, [[5, 6]]), 'answer: 1') 
print(interval_scheduling3(2, [[1, 3], [2, 4], [5, 7], [6, 8]]), 'answer: 4') 
print(interval_scheduling3(1, [[1, 3], [2, 4], [5, 7], [6, 8]]), 'answer: 2') 
print(interval_scheduling3(2, [(3, 64), (18, 34), (20, 90), (22, 74), (57, 94), (58, 81), (59, 100), (67, 90), (82, 91), (87, 97)]), 'answer: 5') 


