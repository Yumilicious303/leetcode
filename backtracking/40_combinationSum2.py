def neetCodeCombinationSum2(candidates, target):
    res = []
    candidates.sort()

    def backtrack(curr, pos, target):
        if target == 0:
            res.append(curr[:])
        if target < 0:
            return
        
        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            backtrack(curr, i + 1, target - candidates[i])
            curr.pop()
            prev = candidates[i]
    backtrack([], 0, target)
    return res

def commentCombinationSum2(candidates, target):
        def backtrack(i, curr, curSum):
            if curSum == target:
                res.append(curr[:])
                return 
            if i >= len(candidates) or curSum > target:
                return
            
            curr.append(candidates[i])
            backtrack(i+1, curr, curSum + candidates[i])
            curr.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            backtrack(i+1, curr, curSum)
                
        candidates.sort() 
        res = []
        backtrack(0, [], 0)
        return res




#print(neetCodeCombinationSum2([10,1,2,7,6,1,5], 8))
print(commentCombinationSum2([10,1,2,7,6,1,5], 8))
#print(neetCodeCombinationSum2([2,3,6,7], 7))
