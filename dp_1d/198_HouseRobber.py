#House Robber
def robNeet(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        nMax = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = nMax
    return rob2

def robRecursive(nums):
    rob_dict = {}
    def dfs(n):
        if n < 0:
            return 0
        if n in rob_dict:
            return rob_dict[n]
        money = max(nums[n]+ dfs(n - 2), dfs(n - 1))
        rob_dict[n] = money
        return money
    return dfs(len(nums) - 1)



print(robRecursive([1,2,3,1]))
print(robRecursive([2,7,9,3,1]))
