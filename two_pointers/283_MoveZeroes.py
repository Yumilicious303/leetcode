#Move Zeroes
def moveZeroes(nums):
    first_zero = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[first_zero], nums[i] = nums[i], nums[first_zero]
            first_zero += 1
    return nums

print(moveZeroes([0,1,0,3,12]))