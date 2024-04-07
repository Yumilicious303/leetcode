#Non-overlapping Intervals
def eraseOverlapIntervals(intervals):
    res = 0
    intervals.sort()
    maxEnd = float('-inf')
    for start, end in intervals:
        if start < maxEnd:
            maxEnd = min(end, maxEnd)
            res += 1
        else:
            maxEnd = max(end, maxEnd)
    return res


def eraseOverlapIntervalsNeet(intervals):
    res = 0
    intervals.sort()
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res





print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))