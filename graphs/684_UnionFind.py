#Union Find
def findRedundantConnectionNeet(edges):
    parent = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)
    
    def find(n):
        p = parent[n]

        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    #return False if can't complete
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]
        

def findRedundantConnectionComment(edges):
    # variables
    n = len(edges)
    parents = [i for i in range(n + 1)]
    def find_group_root(node):
        group_root = node
        while group_root != parents[group_root]:
            group_root = parents[group_root]
        return group_root
    
    for v1, v2 in edges:
        group_root1 = find_group_root(v1)
        group_root2 = find_group_root(v2)
        if group_root1 == group_root2:
            return [v1, v2]
        # union two groups
        parents[group_root2] = group_root1

print(findRedundantConnectionNeet([[1,2],[1,3],[2,3]]))