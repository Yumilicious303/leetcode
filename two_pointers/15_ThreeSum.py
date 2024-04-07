#3Sum (Three Sum)
def threeSum(nums):
    nums.sort()
    res = []
    
    prev = None
    for i in range(len(nums)):
        if nums[i] == prev:
            continue

        target = -nums[i]
        l, r = i + 1, len(nums) - 1
        twoPointPrev = None
        
        while l < r:
            if nums[r] + nums[l] > target:
                twoPointPrev = nums[r]
                r = r - 1
            elif nums[r] + nums[l] < target:
                twoPointPrev = nums[l]
                l = l + 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                twoPointPrev = nums[l]
                l = l + 1
                while l < r and nums[l] == twoPointPrev:
                    l = l + 1
        prev = nums[i]
    return res

def threeSumNeet(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


print(threeSum([-4,-1,-1,0,1,2]))
print(threeSum([-8,0,3,3,5,8]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
