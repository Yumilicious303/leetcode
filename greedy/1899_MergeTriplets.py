#Merge Triplets
def mergeTriplets(triplets, target):
    one, two, three = False, False, False

    for t1, t2, t3 in triplets:
        if any([t1 > target[0], t2 > target[1], t3 > target[2]]):
            continue
        
        if t1 == target[0]:
            one = True
        if t2 == target[1]:
            two = True
        if t3 == target[2]:
            three = True
    
    return True if all([one, two, three]) else False

def mergeTripletsNeet(triplets, target):
    good = set()

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        
        for i, n in enumerate(t):
            if n == target[i]:
                good.add(i)
    
    return len(good) == 3





print(mergeTripletsNeet([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))
print(mergeTripletsNeet([[3,4,5],[4,5,6]], [3,2,5]))
print(mergeTripletsNeet([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))