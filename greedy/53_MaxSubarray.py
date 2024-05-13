#Maximum Subarray
def maxSubArray(nums):
    res = nums[0]
    curr = 0
    for n in nums:
        curr += n
        res = max(res, curr)
        if curr < 0:
            curr = 0
    return res


#print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

print(maxSubArray([-2,-3,-1]))