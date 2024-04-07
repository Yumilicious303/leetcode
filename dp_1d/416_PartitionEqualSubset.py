#Partition Equal Subset Sum
def canPartition(nums):
    def dfs(i, curSum):
        if (curSum, i) in memo:
            return memo[(curSum, i)]
        if curSum == target:
            return True
        if i >= len(nums) or curSum > target:
            return False
        
        if dfs(i + 1, curSum + nums[i]): return True
        if dfs(i + 1, curSum): return True

        memo[(curSum, i)] = False
        return False
    
    if sum(nums) % 2 != 0:
        return False
    
    target = sum(nums) / 2
    memo = {}
    return dfs(0, 0)


def canPartitionNeet(nums):
    if sum(nums) % 2:
        return False
    
    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums)):
        nextDP = set()
        for t in dp:
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    return True if target in dp else False



print(canPartitionNeet([1,5,11,5]))
print(canPartitionNeet([1,2,3,5]))
print(canPartitionNeet([2,2,1,1]))
print(canPartitionNeet([1,2,5]))
print(canPartitionNeet([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))
print(canPartitionNeet([83,12,15,68,83,71,72,99,66,75,53,74,30,65,95,40,22,4,67,61,55,63,85,81,67,10,93,24,24,43,29,88,94,97,27,87,51,12,26,47,10,21,16,2,8,20,94,19,66,6,13,68,27,45,90,20,47,53,71,89,75,88,88,92,12,85,22,74,82,38,2,74,21,16,29,9,9,24,23,76,24,70,64,89,78,84,76,84,95,9,75,62,94,84,48,57,82,26,47,95]))

