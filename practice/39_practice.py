def combinationSum(candidates, target):
    res = []
    cur = []
    def dfs(target, i):
        if target < 0 or i >= len(candidates):
            return
        if target == 0:
            res.append(cur[:])
            return

        cur.append(candidates[i])
        dfs(target - candidates[i], i)
        cur.pop()

        dfs(target, i + 1)
    
    dfs(target, 0)
    return res

print(combinationSum([2,3,6,7], 7))
