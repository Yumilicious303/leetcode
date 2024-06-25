#Course Schedule
from collections import deque
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
    
def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Create a prerequisite dict. (containing courses (nodes) that need to be taken (visited)
	# before we can visit the key.
    prereq = {i: set() for i in range(numCourses)}
	# Create a graph for adjacency and traversing.
    next = {i: set() for i in range(numCourses)}
    for course, pre in prerequisites:
	    # Preqs store requirments as their given.
        prereq[course].add(pre)
		# next stores courses that pre is a prerequisite for
        next[pre].add(course)
    
    q = deque()
	# We need to find a starting location, aka courses that have no prereqs.
    for course, pre in prereq.items():
        if not pre: q.append(course)
	# Keep track of which courses have been taken.
    taken = []
    while q:
        course = q.popleft()
        taken.append(course)
		# If we have visited the numCourses we're done.
        if len(taken) == numCourses:
            return taken
		# For neighboring courses.
        for nextCourse in next[course]:
		    # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
            prereq[nextCourse].remove(course)
			# If we've taken all of the preqs for the new course, we'll visit it.
            if not prereq[nextCourse]:
                q.append(nextCourse)
	# If we didn't hit numCourses in our search we know we can't take all of the courses.
    return []

def findOrderNeet(numCourses, prerequisites):
    prereq = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        prereq[course].append(pre)
    
    taken = []
    taken_set = set()
    cycle = set()
        
    def dfs(course):
        if course in cycle:
            return False
        if course in taken_set:
            return True
        
        
        cycle.add(course)
        for pre in prereq[course]:
            if dfs(pre) is False: return False
        
        cycle.remove(course)
        taken.append(course)
        taken_set.add(course)
        return True


    for c in range(numCourses):
        if dfs(c) is False:
            return []
    return taken


    


print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(2, [[1,0]]))
print(findOrder(2, []))