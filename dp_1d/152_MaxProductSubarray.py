#Max PProduct Subarray 
import time
def maxProduct(nums):
    def dfs(product, i):
        if i >= len(nums):
            return product
        product *= nums[i]
        return max(product, dfs(product, i + 1))

    maxP = nums[0]
    for i in range(len(nums)):
        maxP = max(dfs(1, i), maxP)
    return maxP


def maxProductNeet(nums):
    res = max(nums)
    curMax, curMin = 1, 1
    for n in nums:
        if n == 0:
            curMin = curMax = 1
            continue
        temp = curMax * n
        curMax = max(curMax * n, n * curMin, n)
        curMin = min(temp, curMin * n, n)
        
        res = max(curMax, res)
    return res

def maxProduct2(nums):
    curMax = curMin = res = nums[0]
    for n in nums[1:]:
        curMax, curMin = max(curMax * n, n * curMin, n), min(curMax * n, n * curMin, n)
        res = max(curMax, res)
    return res


print(maxProduct2([2,3,-2,4]))
print(maxProduct2([-2, 0, -1]))
print(maxProduct2([1]))
print(maxProduct2([0, 2]))
print(maxProduct2([-1, -2, -3, 0, 3, 5]))
print(maxProduct2([-1,4,-4,5,-2,-1,-1,-2,-3]))




#print(f'Completion time, Neetcode: {(endNeet - startNeet) * 1000}, Me:{(endme - startme) * 1000}')

