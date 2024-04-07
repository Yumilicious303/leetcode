#House Robber II
def robNeet(nums):
    def helper(houses):
        rob1, rob2 = 0, 0

        for n in houses:
            nMax = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = nMax
        return rob2
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def robRecursive(nums):
    def helper(houses):
        rob_dict = {}
        def dfs(n):
            if n in rob_dict:
                return rob_dict[n]
            if n < 0:
                return 0
            
            money = max(houses[n] + dfs(n - 2), dfs(n - 1))
            rob_dict[n] = money
            return money
        return dfs(len(houses) - 1)
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
    





print(robNeet([1,2,3,1]))
print(robNeet([2,7,9,3,1]))
print(robNeet([2,3,2]))
print(robNeet([1,2,3,1]))
print(robNeet([0]))
print(robNeet([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))