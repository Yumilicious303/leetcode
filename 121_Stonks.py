#Best Time to Buy and Sell Stock
def maxProfit(prices):
    bestBuy = prices[0]
    profitMax = 0
    for price in prices:
        if price < bestBuy:
            bestBuy = price
        
        profitMax = max(profitMax, (price - bestBuy))

    return profitMax

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))