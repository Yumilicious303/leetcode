#Meeting Rooms
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals):
        intervals.sort(key = lambda i : i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
        if i1.end > i2.start:
            return False
        return True




def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

print(canAttendMeetings([(0,30),(5,10),(15,20)]))
print(canAttendMeetings([(15,20),(0,30),(5,10)]))
print(canAttendMeetings([(5,10)]))
print(canAttendMeetings([(5,8),(9,15)]))
print(canAttendMeetings([(0,8),(8,10)]))
print(canAttendMeetings([(0,8),(8,10)]))