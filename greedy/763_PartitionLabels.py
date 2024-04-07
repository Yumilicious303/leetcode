#Partition Labels
def partitionLabels(s):
    firstAppearance = {}
    stack = []

    for i, c in enumerate(s):
        if c not in firstAppearance:
            firstAppearance[c] = i
            stack.append([i, i, 1]) #start of partion, end of partition, length of partition
        else:
            start = i
            while stack and start > firstAppearance[c]:
                start = stack.pop()[0]
            stack.append([start, i, i - start + 1])

    return [i[2] for i in stack]

def partitionLabelsNeet(s):
    lastIndex = {}

    for i, c in enumerate(s):
        lastIndex[c] = i
    
    res = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])
    
        if i == end:
            res.append(size)
            size = 0
    return res


print(partitionLabelsNeet("eccbbbbdec"))
print(partitionLabelsNeet("ababcbacadefegdehijhklij"))