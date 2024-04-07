#Meeting Rooms II
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



def minMeetingRooms(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key= lambda i: i[0])
    rooms = 1
    first_availability = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < first_availability:
            rooms += 1
        first_availability = min(intervals[i][1], first_availability)
    
    return rooms

def minMeetingRooms2(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key= lambda interval: interval.start)
    rooms = 1
    first_availability = intervals[0].end

    for i in range(1, len(intervals)):
        if intervals[i].start < first_availability:
            rooms += 1
        first_availability = min(intervals[i].end, first_availability)
    
    return rooms

def minMeetingRoomsNeet(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


def tupleToIntervals(intervals):
    res = []
    for i in range(len(intervals)):
        interval = Interval(intervals[i][0], intervals[i][1])
        res.append(interval)
    return res



test_cases = [
    [(0,30), (5,10), (15,20)],
    [(5,10), (15,20)],
    [(0, 10), (5, 15), (15, 20)],
    [(0, 5), (5, 10), (10, 15)],
    [(0, 10), (1, 5), (2, 7), (3, 8)],
    [(0, 5)],
    [],
    [(0, 5), (3, 10), (8, 15)],
    [(0, 5), (2, 7), (4, 9), (8, 12), (10, 15)],
    [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)],
    [(0, 10), (5, 15), (10, 20), (15, 25)],
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
]

for case in test_cases:
    intervals = tupleToIntervals(case)
    print(minMeetingRooms(case), minMeetingRooms2(intervals), minMeetingRoomsNeet(intervals))



meetings = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 12),
    (12, 13),
    (13, 14),
    (14, 15),
    (15, 16),
    (16, 17),
    (17, 18),
    (18, 19),
    (19, 20),
    (20, 21),
    (21, 22),
    (22, 23),
    (23, 24),
    (24, 25),
    (25, 26),
    (26, 27),
    (27, 28),
    (28, 29),
    (29, 30),
    (30, 31),
    (31, 32),
    (32, 33),
    (33, 34),
    (34, 35),
    (35, 36),
    (36, 37),
    (37, 38),
    (38, 39),
    (39, 40),
    (40, 41),
    (41, 42),
    (42, 43),
    (43, 44),
    (44, 45),
    (45, 46),
    (46, 47),
    (47, 48),
    (48, 49),
    (49, 50),
    (50, 51),
    (51, 52),
    (52, 53),
    (53, 54),
    (54, 55),
    (55, 56),
    (56, 57),
    (57, 58),
    (58, 59),
    (59, 60),
    (60, 61),
    (61, 62),
    (62, 63),
    (63, 64),
    (64, 65),
    (65, 66),
    (66, 67),
    (67, 68),
    (68, 69),
    (69, 70),
    (70, 71),
    (71, 72),
    (72, 73),
    (73, 74),
    (74, 75),
    (75, 76),
    (76, 77),
    (77, 78),
    (78, 79),
    (79, 80),
    (80, 81),
    (81, 82),
    (82, 83),
    (83, 84),
    (84, 85),
    (85, 86),
    (86, 87),
    (87, 88),
    (88, 89),
    (89, 90),
    (90, 91),
    (91, 92),
    (92, 93),
    (93, 94),
    (94, 95),
    (95, 96),
    (96, 97),
    (97, 98),
    (98, 99),
    (99, 100)
]

#print(min_meeting_rooms(meetings))