#Unique Paths
import time
def uniquePaths(m, n):
    dict = {}
    def dfs(m,n):
        if (m, n) in dict:
            return dict[(m, n)]
        if m == 1 or n == 1:
            return 1
        
        dict[(m,n)] = dfs(m - 1, n) + dfs(m, n - 1)
        return dict[(m, n)]
    
    return dfs(m,n)

def uniquePaths2(m, n, dict):
    if (m, n) in dict:
        return dict[(m, n)]
    if m == 1 or n == 1:
        return 1
    
    dict[(m,n)] = uniquePaths2(m - 1, n, dict) + uniquePaths2(m, n - 1, dict)
    return dict[(m, n)]
    
    
start = time.time()
print(uniquePaths(99, 99))
print(uniquePaths2(99, 99, {}))
end = time.time()
print(f'Time: {(end - start) * 1000}')
