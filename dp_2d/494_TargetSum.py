#Target Sum
def findTargetSumWays(nums, target):
    def dfs(i, total):
        if (i, total) in memo:
            return memo[(i, total)] 
        if i >= len(nums):
            return 1 if total == 0 else 0
            
        memo[(i, total)] = dfs(i + 1, total - nums[i]) + dfs(i + 1, total + nums[i])
        return memo[(i, total)]
    memo = {}
    return dfs(0, target)


print(findTargetSumWays([1,1,1,1,1], 3))
print(findTargetSumWays([1], 1))
