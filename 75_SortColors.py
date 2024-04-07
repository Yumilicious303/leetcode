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
        



print(sortColors([2,0,2,1,1,0]))