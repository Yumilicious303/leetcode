#Single Number
def singleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res

print(singleNumber([4,1,2,1,2]))