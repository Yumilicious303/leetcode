#Jump Game
def canJump(nums):
    neededJump = 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < neededJump: neededJump += 1
        else: neededJump = 1
    return False if neededJump > 1 else True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
