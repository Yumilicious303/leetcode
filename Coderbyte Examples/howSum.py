def howSum(target, nums, curr = None, memo = None):
    if memo is None:
        memo = {}
    if curr is None:
        curr = []
    
    if target in memo:
        return memo[target]
    if target == 0:
        return curr
    if target < 0:
        return None

    for n in nums:
        res = howSum(target - n, nums, curr + [n], memo)
        if res is not None:
            memo[target] = res
            return res
    
    memo[target] = None
    return None




print(howSum(7, [5,3,4,7]))
print(howSum(7, [5,3,9,6]))
print(howSum(0, [1,2,3]))