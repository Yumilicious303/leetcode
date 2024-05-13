#Trapping Rain Water
def trap(height):
    potentialWater = [0] * (max(height) + 1)
    maxHeight = 0
    actualWater = 0

    for h in height:
        maxHeight = max(maxHeight, h)
        #make any potential water actual water
        for p in range(1, h + 1):
            actualWater = actualWater + potentialWater[p]
            potentialWater[p] = 0
        #count potential water
        for p in range(h + 1, maxHeight + 1):
            potentialWater[p] = potentialWater[p] + 1
    return actualWater

def trap2(height):
    maxright = len(height) * [0]
    maxleft = 0
    total = 0
    
    for x in range(len(height) - 1, -1, -1):
        if x < len(height) - 1:
            maxright[x] = max(maxright[x + 1], height[x + 1])
    for i in range(0, len(height) - 1):
        water = min(maxleft, maxright[i]) - height[i]
        if water > 0:
            total = total + water
        maxleft = max(maxleft, height[i])
    return total


def trapNeet(height):
    if not height: return 0
    
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res


            
    
print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap2([4,2,0,3,2,5]))


