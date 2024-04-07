#Minimum Deletions
from collections import Counter
def minDeletions(s):
    res = 0
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    
    vals = list(counter.values())
    freq = [0] * (max(vals) + 1)
    for v in vals:
        freq[v] += 1

    carryDown = 0
    for i in range(len(freq) - 1, 0, -1):
        freq[i] += carryDown
        carryDown = 0
        if freq[i] > 1:
            carryDown = freq[i] - 1
            freq[i] = 1
        res += carryDown
    return res

def minDeletionsNeet(s):
    count = Counter(s)
    used_freq = set()
    res = 0

    for c, freq in count.items():
        while freq > 0 and freq in used_freq:
            freq -= 1
            res += 1
        used_freq.add(freq) # freq = either unique or 0
    return res

print(minDeletionsNeet('aab'))
print(minDeletionsNeet('ccaaffddecee'))
print(minDeletionsNeet('aaabbbcc'))
 