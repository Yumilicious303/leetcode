import sys

for line in sys.stdin:
    input = line.split()
    l, r = input
    l, r = int(l), int(r)
    if l == 0 and r == 0: print("Not a moose")
    elif l == r: print(f'Even {l + r}')
    else: print(f'Odd {2 * max(l, r)}')

'''
The problem is essentially asking if you can take a word problem and turn it into a conditional statement. Probably the trickiest part of this problem is just figuring out how Kattis gives you your input and how it wants its output. 
'''

'''
The first part is just converting the given input into a format I can easily work with.
The conditions are:
- If both l and r are 0, this is not a moose.
- If l and r are equal (and not 0, as evaluated by the previous condition; order of the statements here is important) then this is an Even moose and its points are the sum of l and r.
- Otherwise (this is the case where we have a moose, but the number of tines on the left and right are different) we have an Odd moose its points are double the maximum of l and r.
'''

import sys
import heapq

intervals = []

#getting the input and putting it into array form
for line in sys.stdin:
    input = line.split()
    x, y = input
    x, y = int(x), int(y)
    intervals.append([x, y])

#extracting info from the first line, since it represents n and k rather than x and y
total_kittens, total_beds = intervals[0]
#getting rid of the first element. Doing it this way means it's an O(1) operation
intervals[0] = intervals[-1]
intervals.pop()

#We need to sort the array in ascending order based on arrival time. O(nlogn) operation.
intervals.sort()
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
print(res)