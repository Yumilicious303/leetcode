#Climbing Stairs
def climbStairs(n): #Each time you can either climb 1 or 2 steps.
    dict = {}
    def dfs(i):
        if i in dict:
            return dict[i]
        
        if i == 0 or i == 1:
            return 1
        
        stairs = dfs(i - 1) + dfs(i - 2)

        dict[i] = stairs

        return stairs
    return dfs(n)

def climbStairsII(n): #Each time you can either climb 1 or 2 or 3 steps.
    dict = {}
    def dfs(i):
        if i in dict:
            return dict[i]
        
        if i == 0 or i == 1:
            return 1
        
        if i == 2:
            return 2
        
        stairs = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)

        dict[i] = stairs

        return stairs
    return dfs(n)




print(climbStairsII(5))



     