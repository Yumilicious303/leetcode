#Combination Sum
def mycombinationSum(candidates, target):
    res = []
    def backtrack(currentSum, curr):
        if currentSum == target:
            res.append(curr[:])
            return
        
        for can in candidates:
            if can + currentSum <= target:
                currentSum = currentSum + can
                curr.append(can)
                backtrack(currentSum, curr)
                curr.pop()
                currentSum = currentSum - can
    
    backtrack(0, [])
    return res

def neetcodeCombinationSum(candidates, target):
    res = []
    def backtrack(i, curr, currentSum):
        if currentSum == target:
            res.append(curr[:])
            return
        if i >= len(candidates) or currentSum > target:
            return
        
        curr.append(candidates[i])
        backtrack(i, curr, currentSum + candidates[i])
        curr.pop()
        backtrack(i + 1, curr, currentSum)
    
    backtrack(0, [], 0)
    return res

def commentCombinationSum(candidates, target):
    res = []
    def backtrack(i, cur):
        cursum = sum(cur)
        if cursum == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or cursum > target:
            return
        
        for j in range(i, len(candidates)):
            backtrack(j, cur + [candidates[j]])
        
    backtrack(0, [])
    return res



#print(mycombinationSum([2,3,6,7], 7))
#print(neetcodeCombinationSum([2,3,6,7], 7))
#print(neetcodeCombinationSum([2,3,5], 8))
print(commentCombinationSum([2,3,6,7], 7))

