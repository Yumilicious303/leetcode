#Contains Duplicate
def containsDuplicate(nums):
    nums.sort()
    if len(nums) <= 1:
        return False
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

def containsDuplicate2(nums):
    numSet = set(nums)
    if len(numSet) == len(nums):
        return False
    else: return True

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(containsDuplicate2([1,2,3,1]))
print(containsDuplicate2([1,2,3,4]))
print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))


        