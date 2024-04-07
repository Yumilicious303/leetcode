#Time Based Key-Value Store
class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        
        l, r = 0, len(self.store[key]) - 1
        next_highest = None
        while l <= r:
            m = (r + l) // 2
            if self.store[key][m][0] > timestamp:
                r = m - 1
            elif self.store[key][m][0] < timestamp:
                l = m + 1
                if next_highest:
                    if next_highest[0] < self.store[key][m][0]:
                        next_highest = (self.store[key][m][0], self.store[key][m][1])
                else:
                    next_highest = (self.store[key][m][0], self.store[key][m][1])
            else:
                return self.store[key][m][1]
        if next_highest:
            return next_highest[1]
        else:
            return ""

class TimeMapNeet(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])

        #binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


def test_case1():
    timeMap = TimeMapNeet()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 4))

def test_case2():
    timeMap = TimeMapNeet()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    print(f'Output: {timeMap.get("love", 5)}, Expected: ""')
    print(f'Output: {timeMap.get("love", 10)} Expected: high')
    print(f'Output: {timeMap.get("love", 15)} Expected: high')
    print(f'Output: {timeMap.get("love", 20)} Expected: low')
    print(f'Output: {timeMap.get("love", 25)} Expected: low')

test_case2()
    

