#Reorganize String
import heapq

def reorganizeString(s):
    res = ''
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    heap = []
    for char, count in counter.items():
        heap.append([-count, char])
    heapq.heapify(heap)

    prev = None
    while heap or prev:
        if prev and not heap:
            return ''
        count, char = heapq.heappop(heap)
        res += char
        count += 1

        if prev:
            heapq.heappush(heap, prev)
            prev = None
        if count != 0:
            prev = [count, char]
    return res



print(reorganizeString('aaab'))