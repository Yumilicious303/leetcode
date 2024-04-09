#Sort Colors
def sortColors(nums):
    count = [0,0,0]

    for n in nums:
        count[n] = count[n] + 1
    n = 0
    i = 0
    while i < len(count):
        if count[i] == 0:
            i = i + 1
            continue

        nums[n] = i
        n = n + 1
        count[i] = count[i] - 1

    return nums

def sortColors2(nums):
    colorCount = [0, 0, 0]
    for n in nums:
        colorCount[n] += 1
    
    color = 0
    for i in range(len(nums)):
        while colorCount[color] == 0: 
            color += 1
        
        nums[i] = color
        colorCount[color] -= 1
    return nums

def sortColorsNeet(nums):
    l, r = 0, len(nums) - 1
    i = 0

    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1
    return nums
        



print(sortColorsNeet([2,0,2,1,1,0]))