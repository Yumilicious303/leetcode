def bestSum(target, nums):
    res = []
    memo = set()
    def dfs(currValue, curr_nums):
        nonlocal res
        if currValue in memo:
            return
        if res and len(curr_nums) > len(res):
            return
        if currValue > target:
            return
        if currValue == target and target > 0:
            if (res and len(curr_nums) < len(res)) or not res:
                res = curr_nums[:]
        for n in nums:
            dfs(currValue + n, curr_nums + [n])
            #memo.add(currValue)


    dfs(0, [])
    return res


def bestSum2(targetSum, nums, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for n in nums:
        remainder = targetSum - n
        remainderCombination = bestSum2(remainder, nums, memo)
        if remainderCombination is not None:
            combination = remainderCombination[:] + [n]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    
    memo[targetSum] = shortestCombination
    return shortestCombination

    



#print(bestSum(7, [3,4,5,7]))
#print(bestSum(0, [3,4,5,7]))
print(bestSum2(0, [1]))
print(bestSum2(3, [7]))

            
