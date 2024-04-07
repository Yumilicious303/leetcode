#Two Sum II
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while numbers[l] + numbers[r] != target:
        if numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return [l + 1, r + 1]

def twoSumNeet(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [1 + 1, r + 1]


print(twoSum([1,3,4,5,7,10,11], 9))