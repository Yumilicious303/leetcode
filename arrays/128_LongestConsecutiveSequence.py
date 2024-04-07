#Longest Consecutive Sequence
def longestConsecutive(nums):
    nums.sort()
    prev = None
    longest = 0
    curr = 0
    for num in nums:
        if prev is not None and num == prev + 1:
            curr += 1
            longest = max(longest, curr)
        elif num == prev:
            pass
        else:
            curr = 1
            longest = max(longest, curr)
        prev = num
    return longest

def longestConsecutive2(nums):
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if (num - 1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
                longest = max(length, longest)
    return longest






x = [100,4,200,1,3,2]
y = [0,3,7,2,5,8,4,6,0,1]
z = [1]

print(longestConsecutive2(x))
print(longestConsecutive2(y))
print(longestConsecutive2(z))