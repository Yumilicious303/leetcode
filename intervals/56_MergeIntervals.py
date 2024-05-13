#Merge Intervals
def merge(intervals):
    intervals.sort()
    res = []
    for start, end in intervals:
        if res and res[-1][1] >= start:
            prevStart, prevEnd = res.pop()
            start, end = prevStart, max(end, prevEnd)
        res.append([start, end])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))