def trap(height):
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]
    res = 0

    while l < r:
        if height[l] <= height[r]:
            water = min(maxL, maxR) - height[l]
            if water > 0:
                res += water
            l += 1
            maxL = max(maxL, height[l])
        else:
            water = min(maxL, maxR) - height[r]
            if water > 0:
                res += water
            r -= 1
            maxR = max(maxR, height[r])
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))