#Coin Change
def change(amount, coins):
    def dfs(i, amount):
        if (i, amount) in memo:
            return memo[(i, amount)]
        if amount == 0:
            return 1
        if amount < 0 or i >= len(coins):
            return 0
        
        memo[(i, amount)] = dfs(i + 1, amount) + dfs(i, amount - coins[i])
        return memo[(i, amount)]
    
    memo = {}
    return dfs(0, amount)

def changeDP(amount, coins):
    dp = [[0 for i in range(amount + 1)] for i in coins]
    for r in range(len(coins) - 1, -1, -1):
        for c in range(amount, -1, -1):
            if c == amount:
                dp[r][c] = 1
                continue
    for i in dp:
        print(i)

def changeNeet(amount, coins):
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]

    for i in dp:
        print(i)

def changeNeetMine(amount, coins):
    dp = [[0] * len(coins) for i in range(amount + 1)]
    dp[0] = [1] * len(coins)

    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1] if i < len(coins) - 1 else 0
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]

    for i in dp:
        print(i)






print(changeNeetMine(5, [1,2,5]))
#print(changeDP(3, [2]))
#print(changeDP(10, [10]))
#print(changeDP(500, [3,5,7,8,9,10,11]))