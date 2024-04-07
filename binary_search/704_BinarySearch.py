#Binary Search
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        #m = l + r // 2
        m = ((r - l) // 2) + l
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

print(search([-1,0,3,5,9,12], 12))