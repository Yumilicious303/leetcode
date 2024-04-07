#Happy Number
def isHappy(n):
    curSum = n
    visited = set()
    while curSum != 1:
        if curSum in visited:
            return False
        visited.add(curSum)
        temp = 0
        for d in str(curSum):
            temp += int(d)**2
        curSum = temp
    return True

def isHappy2(n):
    visited = set()
    while n != 1:
        if n in visited:
            return visited
        visited.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True

#for i in range(101):
#    print(f'{i}: {isHappy2(i)}')

print(isHappy2(52563))