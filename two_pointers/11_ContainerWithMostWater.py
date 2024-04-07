#Container with Most Water
def maxArea(height):
    l, r = 0, len(height) - 1
    maxWater = 0
    while l < r:
        water = (r - l) * min(height[r], height[l])
        maxWater = max(water, maxWater)
        if height[l] <= height[r]:
            l = l + 1
        else:
            r = r - 1
    return maxWater

print(maxArea([1,8,6,2,5,4,8,3,7]))