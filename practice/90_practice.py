def subsetsWithDup(nums):
    nums.sort()
    res = []
    def dfs(i, cur):
        if i >= len(nums):
            res.append(cur[:])
            return
        
        cur.append(nums[i])
        dfs(i + 1, cur)
        cur.pop()

        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        dfs(i + 1, cur)

    dfs(0, [])
    return res

print(subsetsWithDup([1,2,2]))



