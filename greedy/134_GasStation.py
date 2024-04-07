#Gas Station
def canCompleteCircuit(gas, cost):
    for g in range(len(gas)):
        tank = 0
        pos = g
        while True:
            tank += gas[pos]
            costtogettonextstation = cost[pos]
            if pos == len(gas) - 1:
                pos = 0
            else:
                pos += 1
            
            if costtogettonextstation > tank:
                break
            
            tank -= costtogettonextstation

            if pos == g:
                return g
    return - 1

def canCompleteCircuitNeet(gas, cost):
    if sum(cost) > sum(gas):
        return - 1
    
    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            res = i + 1
    return res
    


#print(canCompleteCircuitNeet([1,2,3,4,5], [3,4,5,1,2]))
print(canCompleteCircuitNeet([5,1,2,3,4], [4,4,1,5,1]))

#print(canCompleteCircuitNeet([2,3,4], [3,4,3]))
#print(canCompleteCircuitNeet([5], [2]))
#print(canCompleteCircuitNeet([31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]))
            
