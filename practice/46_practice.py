def permute(nums):
    res = []
    def dfs(cur):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        
        for n in nums:
            if n not in cur:
                cur.append(n)
                dfs(cur)
                cur.pop()
    dfs([])
    return res

print(permute([1, 2, 3]))