def canSum(target, nums, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    
    for n in nums:
        if canSum(target - n, nums, memo):
            memo[target] = True
            return True
    
    memo[target] = False
    return False

print(canSum(7, [5,3,4,7]))
print(canSum(7, [5,3,9,6]))
print(canSum(300, [7,14]))