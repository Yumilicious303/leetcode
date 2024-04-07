#Two Sum
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            answer = [dict[complement], i]
            return answer
        else:
            dict[nums[i]] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
