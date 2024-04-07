#Course Schedule
def canFinish(numCourses, prerequisites):
    graph = {}
    visited = set()
    for course in range(numCourses):
        graph[course] = []
    for course, pre in prerequisites:
        graph[course].append(pre)
    
    def dfs(course):
        if course in visited:
            return False
        if len(graph[course]) == 0:
            return True
        visited.add(course)
        
        for n in graph[course]:
            if not dfs(n): return False
            
        visited.remove(course)
        graph[course] = []
        return True
    
    for course in range(numCourses):
        if not dfs(course): return False
    return True
    



print(canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
print(canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))