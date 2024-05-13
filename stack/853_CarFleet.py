#Car Fleets
def carFleet(target, position, speed):
    fleets = 0
    for i in range(len(position)):
        time_to_target = (target - position[i]) / speed[i]
        position[i] = [position[i], time_to_target]
    position.sort()
    

    prev = None
    for i in range(len(position) - 1, -1, -1):
        if not prev or position[i][1] > prev:
            fleets += 1
            prev = position[i][1]
    
    return fleets


def carFleetNeet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)




    

    return position

print(carFleetNeet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(carFleetNeet(10, [6,8], [3,2]))
print(carFleetNeet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))

