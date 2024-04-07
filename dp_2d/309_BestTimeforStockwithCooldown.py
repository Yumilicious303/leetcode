#Best Time to Buy and Sell Stock with Cooldown
def maxProfit(prices):
    def dfs(i, state):
        if (i, state) in memo:
            return memo[(i, state)]
        if i >= len(prices):
            return 0
        if state == 'have_stock':
            max_p = max(dfs(i + 1, 'cooldown') + prices[i], dfs(i + 1, 'have_stock'))
        elif state == 'no_stock':
            max_p = max(dfs(i + 1, 'have_stock') - prices[i], dfs(i + 1, 'no_stock')) 
        elif state == 'cooldown':
            max_p = dfs(i + 1, 'no_stock')
        memo[(i, state)] = max_p
        return max_p
    memo = {}
    return dfs(0, 'no_stock')


def maxProfit(prices):
    # State: Buying or Selling?
    # If Buy -> i + 1
    # If Sell -> i + 2
    dp = {}  # key=(i, buying) val=max_profit
    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]
        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]
    return dfs(0, True)
            



print(maxProfit([1,2,3,0,2]))
#print(maxProfit([48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]))
print(maxProfit([2, 1, 4]))