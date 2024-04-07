#Course Schedule
def findOrder(numCourses, prerequisites):
    def dfs(course):
        if course in appended:
            return
        if course in visited:
            return False
        
        visited.add(course)
        for p in prereq_map[course]:
            if dfs(p) is False:
                return False
        visited.remove(course)

        prereq_map[course] = []

        res.append(course)
        appended.add(course)


    prereq_map = {}
    res = []
    appended = set()
    visited = set()

    #organize into dictionary
    for n in range(numCourses):
        prereq_map[n] = []
    for p in prerequisites:
        prereq_map[p[0]].append(p[1])


    for p in prereq_map.keys():
        if dfs(p) is False:
            return []
    return res
    


def findOrderNeet(numCourses, prerequisites):
    prereq = {c:[] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)
    
    res = []
    appended = set()
    cycle = set()
        
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in appended:
            return True
        
        
        cycle.add(crs)
        for p in prereq[crs]:
            if dfs(p) is False:
                return False
        cycle.remove(crs)
        res.append(crs)
        appended.add(crs)
        return True


    for c in range(numCourses):
        if dfs(c) is False:
            return []
    return res


    


print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(2, [[1,0]]))
print(findOrder(2, []))