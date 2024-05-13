#Fruit Baskets
from collections import defaultdict
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


def totalFruit(fruits):
    l, res, curTotal = 0, 0, 0
    curBaskets = defaultdict(int)

    for r in range(len(fruits)):
        curBaskets[fruits[r]] += 1
        curTotal += 1

        while len(curBaskets) > 2:
            f = fruits[l]
            curBaskets[f] -= 1
            curTotal -= 1
            if curBaskets[f] == 0:
                del curBaskets[f]
            l += 1

        res = max(curTotal, res)
    return res

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))