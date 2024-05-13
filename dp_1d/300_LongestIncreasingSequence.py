#Longest Increasing Sequence
def lengthOfLIS(nums): #DP Solution (Probably stick with this one)
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

def lengthOfLIS2(nums): #Binary Search Solution
	tails = [0] * len(nums)
	result = 0
	for num in nums:
		left_index, right_index = 0, result
		while left_index != right_index:
			middle_index = left_index + (right_index - left_index) // 2
			if tails[middle_index] < num:
				left_index = middle_index + 1
			else:
				right_index = middle_index
		result = max(result, left_index + 1)
		tails[left_index] = num
	return result

#print(lengthOfLIS2([10,9,2,5,3,7,101,18]))
print(lengthOfLIS2([10,9]))
