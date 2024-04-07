def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    def dfs(i, cur, target):
        if target == 0:
            res.append(cur[:])
            return
        if target < 0 or i >= len(candidates):
            return
        
        cur.append(candidates[i])
        dfs(i + 1, cur, target - candidates[i])
        cur.pop()

        while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1
        dfs(i + 1, cur, target)
    
    dfs(0, [], target)
    return res


print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))