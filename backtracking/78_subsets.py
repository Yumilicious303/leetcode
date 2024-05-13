#Subsets
def subsets(nums):
    def backtrack(i):
        if i >= len(nums):
            answer.append(curr[:])
            return
    
        curr.append(nums[i])
        backtrack(i + 1)

        curr.pop()
        backtrack(i + 1)

    answer = []
    curr = []
    backtrack(0)
    return answer

def subsets2(nums):
    def backtrack(i, curr):
        if i >= len(nums):
            answer.append(curr)
            return
    
        backtrack(i + 1, curr + [nums[i]])
        backtrack(i + 1, curr)

    answer = []
    backtrack(0, [])
    return answer

def subsetsIterative(nums):
    res = []
    stack = [(0, [])]
    while stack:
        cur_index, cur_subset = stack.pop()
        if cur_index >= len(nums):
            res.append(cur_subset)
            continue
        stack.append((cur_index + 1, cur_subset))
        stack.append((cur_index + 1, cur_subset + [nums[cur_index]]))
    return res





print(subsets([1,2,3]))
print(subsets2([1,2,3]))
print(subsetsIterative([1,2,3]))