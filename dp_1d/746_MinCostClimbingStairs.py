#Min Cost Climbing Stairs
def minCostClimbingStairs(cost):
    dp = [float('inf')] * len(cost) 


    for i in range(len(cost) - 1, -1, -1):
        dp[i] = min(dp[i + 1] if i + 1 in range(len(dp)) else 0, dp[i + 2] if i + 2 in range(len(dp)) else 0) + cost[i]
    
    return min(dp[0], dp[1])

def minCostClimbingStairs2(cost):
    dp = [float('inf')] * len(cost) 

    dp[-1] = cost[-1]
    dp[-2] = cost[-2]

    for i in range(len(cost) - 3, -1, -1):
        dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
    
    return min(dp[0], dp[1])

def minCostClimbingStairsRecursive(cost):
    def dfs(i):
        if i in memo:
            return memo[i]
        if i >= len(cost):
            return 0
        
        memo[i] = min(dfs(i + 1), dfs(i + 2)) + cost[i]
        return memo[i]

    memo = {}
    return min(dfs(0), dfs(1))

def minCostClimbingStairsNeet(cost):
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    
    return min(cost[0], cost[1])



print(minCostClimbingStairsRecursive([10,15,20]))
print(minCostClimbingStairsRecursive([1,100,1,1,1,100,1,1,100,1]))
