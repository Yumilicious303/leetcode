#Merge Intervals
def merge(intervals):
    intervals.sort()
    res = []
    for i in range(len(intervals)):
        if len(res) == 0 or res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1] = ([min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))