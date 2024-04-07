#Graph Valid Tree
def valid_tree(n, edges):
    if n == 0:
        return True
    
    visited = set()
    graph = {i:[] for i in range(n)}
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dfs(node, previous):
        if node in visited:
            return False
        
        visited.add(node)

        for n in graph[node]:
            if n is not previous:
                if not dfs(n, node): return False
        return True


    #return True if dfs(0, None) and len(visited) == n else False
    return dfs(0, None) and len(visited) == n #equivalent to line above



print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

