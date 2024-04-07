def subsets(nums):
    res = set()
    nums.sort()
    def dfs(i, curr):
        if i > len(nums) - 1:
            res.add(tuple(curr))
            return
        
        curr.append(nums[i])
        dfs(i + 1, curr)
        curr.pop()
        dfs(i + 1, curr)
        
        
    dfs(0, [])
    res_list = list(res)
    for r in range(len(res_list)):
        res_list[r] = list(res_list[r])
    return list(res_list)

def subsetsNeet(nums):
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[:])
            return

    #All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
    #All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)
    
    backtrack(0, [])
    return res
    

        






print(subsetsNeet([1,2,2,3]))