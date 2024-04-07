#Coin Change
def coinChange(coins, amount):
    def dfs(target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        if target < 0:
            return -1
        
        minCoins = -1
        
        for c in coins:
            coinsRequired = dfs(target - c, memo)
            if coinsRequired >= 0:
                if minCoins >= 0:
                    minCoins = min(coinsRequired, minCoins)
                else: 
                    minCoins = coinsRequired
        
        if minCoins >= 0:
            memo[target] = minCoins + 1
            return memo[target]
        else:
            memo[target] = minCoins
            return minCoins
    return dfs(amount, {})

def coinChangeNeet(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != amount + 1 else -1









print(coinChangeNeet([1,2,5], 11))
#print(coinChangeNeet([2], 3))
#print(coinChangeNeet([1], 0))
#print(coinChangeNeet([5,3,1], 9))
#print(coinChangeNeet([7,10,5,3], 435))

