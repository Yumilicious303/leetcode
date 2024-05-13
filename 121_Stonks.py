#Best Time to Buy and Sell Stock
def maxProfit(prices):
    minPrice = prices[0]
    maxProfit = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
        maxProfit = max(maxProfit, price - minPrice)
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))