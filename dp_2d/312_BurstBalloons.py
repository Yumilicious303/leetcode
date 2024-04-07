#Burst Balloons
def maxCoins(nums):
    def dfs(remainingBalloons):
        if tuple(remainingBalloons) in memo:
            return memo[tuple(remainingBalloons)]
        if len(remainingBalloons) == 0:
            return 0
        maxC = 0
        for i in range(len(remainingBalloons)):
            left = remainingBalloons[i - 1] if i > 0 else 1
            right = remainingBalloons[i + 1] if i < len(remainingBalloons) - 1 else 1
            maxC = max(maxC, left * right * remainingBalloons[i] + dfs(remainingBalloons[:i] + remainingBalloons[i + 1:]))
        memo[tuple(remainingBalloons)] = maxC
        return maxC
    memo = {}
    x = dfs(nums)
    return x

#print(maxCoins([3,1,5,8]))
print(maxCoins([1, 5]))
print(maxCoins([2, 4]))
print(maxCoins([1, 8]))
#print(maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9]))
            
