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

def uniquePathsDP(m: int, n: int) -> int:
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[-1][-1]



    
    
#start = time.time()
#print(uniquePaths(99, 99))
#print(uniquePaths2(99, 99, {}))
#end = time.time()
#print(f'Time: {(end - start) * 1000}')

print(uniquePathsDP(3, 7))
