#Fruit Baskets
def totalFruit(fruits):
    fruitCounter = {}
    fruitCounterLength = 0
    res = 0
    l = 0

    for r in range(len(fruits)):
        if fruits[r] not in fruitCounter:
            fruitCounter[fruits[r]] = 1
            fruitCounterLength += 1
        else:
            fruitCounter[fruits[r]] += 1

        while fruitCounterLength > 2:
            fruitCounter[fruits[l]] -= 1
            if fruitCounter[fruits[l]] <= 0:
                del fruitCounter[fruits[l]]
                fruitCounterLength -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))