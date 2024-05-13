import sys
import heapq

coworkers = []

#getting the input and putting it into array form
for line in sys.stdin:
    input = line.split()
    a, d = input
    a, d = int(a), int(d)
    coworkers.append([a, d])

#extracting info from the first line, since it represents n and k rather than x and y
help_needed, total_coworkers = coworkers[0]
#getting rid of the first element. Doing it this way means it's an O(1) operation
coworkers[0] = coworkers[-1]
coworkers.pop()

#First we get the max of our initial annoyance values. Even though the problem specifies we have 
#at least one coworker, this means that even if we didn't, we get a correct output. O(n)
res = max(worker[0] for worker in coworkers)
#A min heap is the best data structure for this since we are trying to pick the coworker that will have the
#lowest annoyance level after we ask for help.
potential_annoyance = [[current + increase, increase] for current, increase in coworkers]
heapq.heapify(potential_annoyance)
#Time complexity: O(nlogn)
for i in range(help_needed):
    #Every time we ask for help, we take the lowest potential annoyance, see if it's increased our max,
    #and place the new potential value back in our heap. 
    new_annoyance, increase = heapq.heappop(potential_annoyance)
    res = max(res, new_annoyance)
    heapq.heappush(potential_annoyance, [new_annoyance + increase, increase])
print(res)