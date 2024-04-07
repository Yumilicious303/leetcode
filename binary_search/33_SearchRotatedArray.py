#Search Rotated Array
def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > nums[l]:
            #we're on left side of pivot
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            #we're on the right side of the pivot
            if nums[r] <= target <= nums[r]:
                l = m - 1
            else:
                r = m - 1
    return -1

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        
        if nums[m] >= nums[l]:
            #we're on left side of pivot
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            #we're on the right side of the pivot
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

def searchNeet(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        
        if nums[l] <= nums[m]:
            #we're on left side of pivot
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            #we're on the right side of the pivot
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1

print(searchNeet([4,5,6,7,0,1,2], 0))
print(searchNeet([5,1,3], 2))

