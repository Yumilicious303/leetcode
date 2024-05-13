#Climbing Stairs
def climbStairsIterative(n): #Each time you can either climb 1 or 2 steps, iteratively.
    n1, n2 = 1, 1
    for i in range(2, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


def climbStairs(n): #Each time you can either climb 1 or 2 steps.
    def dfs(n):
        if n in memo: return memo[n]
        if n == 0 or n == 1: return 1
        
        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]
    memo = {}
    return dfs(n)


def climbStairsII(n): #Each time you can either climb 1 or 2 or 3 steps.
    memo = {}
    def dfs(n):
        if n in memo: return memo[n]
        if n == 0 or n == 1: return 1
        if n == 2: return 2

        memo[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
        return memo[n]

    return dfs(n)




print(climbStairsII(5))



     