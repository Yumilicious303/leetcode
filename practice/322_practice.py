def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i - c] + 1, dp[i])
    return dp[amount] if dp[amount] < amount + 1 else -1


print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))