#Find Miniumum of Rotated Array
def findMin(nums):
    l, r = 0, len(nums) - 1
    if nums[l] <= nums[r]:
        return nums[l]
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            #left side of array
            l = m + 1
        else:
            #right side of array
            if nums[m - 1] > nums[m]:
                return nums[m]
            else:
                r = m - 1


def findMinNeet(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
    
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
print(findMin([2,5,1]))
print(findMin([5]))