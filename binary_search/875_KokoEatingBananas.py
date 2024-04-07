#Koko Eating Bananas
import math
def minEatingSpeed(piles, h):
    kRange = [i for i in range(1, max(piles) + 1)]
    k = 1
    res = max(piles)
    for k in kRange:
        hoursTaken = 0
        for pile in piles:
            hoursTaken += math.ceil(pile/k)
        if hoursTaken <= h:
            res = min(res, k)
    return res

def minEatingSpeed2(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        k = (l + r) // 2
        hoursTaken = 0
        for pile in piles:
            hoursTaken += math.ceil(pile/k)
            if hoursTaken > h:
                break
        if hoursTaken > h:
            l = k + 1
        else:
            r = k - 1
            res = min(res, k)
    return res

def minEatingSpeedNeet(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res






print(minEatingSpeedNeet([3,6,7,11], 8))
print(minEatingSpeedNeet([30,11,23,4,20], 5))
print(minEatingSpeedNeet([30,11,23,4,20], 6))