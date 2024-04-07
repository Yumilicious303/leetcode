#Jump Game II
from collections import deque
def jump(nums): #DP solution: O(n^2)
    dp = [float('inf')] * len(nums)
    dp[-1] = 0
    #return dp

    for i in range(len(nums) -1, -1, -1):
        for j in range(i, min(len(nums), i + nums[i] + 1)):
            dp[i] = min(dp[i], dp[j] + 1)
    return dp[0]

def jumpBFS(nums):
    jumps = 0
    queued = {0}
    q = deque([0])
    while q and len(nums) - 1 not in queued:
        for i in range(len(q)):
            jump = q.popleft()
            for j in range(jump + 1, jump + nums[jump] + 1):
                if j not in queued:
                    q.append(j)
                    queued.add(j)
        jumps += 1
    return jumps

def jumpNeet(nums):
    res = l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res





print(jumpBFS([2,3,1,1,4]))
print(jumpBFS([2,3,0,1,4]))
print(jumpBFS([3]))
print(jumpBFS([1,3]))
