#Analyze User Website Visit Pattern
from collections import defaultdict
from collections import Counter
from itertools import combinations

def mostVisitedPattern(username, timestamp, website):
    d = defaultdict(list)

    for t, u, w in sorted(zip(timestamp, username, website)):
        d[u].append(w)

    c = Counter()
    for u in d:
        c += Counter(set(seq for seq in combinations(d[u], 3)))
    target = max(c.values())

    return min(list(k) for k in c if c[k] == target)

def mostVisitedPattern2(username, timestamp, website):
    visitsbyUser = defaultdict(list)

    for t, u, w in sorted(zip(timestamp, username, website)):
        visitsbyUser[u].append(w)

    threeSequencecounter = defaultdict(int)
    for user in visitsbyUser:
        for combo in set(combinations(visitsbyUser[user], 3)):
            threeSequencecounter[combo] += 1
    
    max_sequence, max_count = '', 0
    for sequence, count in threeSequencecounter.items():
        if count > max_count or (count == max_count and sequence < max_sequence):
            max_sequence, max_count = sequence, count
    return max_sequence

def mostVisitedPattern3(username, timestamp, website):
    visitsbyUser = defaultdict(list)

    #for t, u, w in sorted(zip(timestamp, username, website)):
    #    visitsbyUser[u].append(w)

    zipped = [[timestamp[i], username[i], website[i]] for i in range(len(timestamp))]
    zipped.sort()

    for time, user, site in zipped:
        visitsbyUser[user].append(site)

    threeSequencecounter = defaultdict(int)
    for user in visitsbyUser:
        for combo in getCombinations(visitsbyUser[user]):
            threeSequencecounter[combo] += 1
    
    max_sequence, max_count = '', 0
    for sequence, count in threeSequencecounter.items():
        if count > max_count or (count == max_count and sequence < max_sequence):
            max_sequence, max_count = sequence, count
    return max_sequence

def getCombinations(websites):
    combos = set()
    for first in range(len(websites)):
        for second in range(first + 1, len(websites)):
            for third in range(second + 1, len(websites)):
                combos.add((websites[first], websites[second], websites[third]))
    return combos



username1 = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp1 = [1,2,3,4,5,6,7,8,9,10]
website1 = ["home","about","career","home","cart","maps","home","home","about","career"]

username2 = ['h', 'eiy', 'cq', 'h', 'cq', 'txldsscx', 'cq', 'txldsscx', 'h', 'cq', 'cq']
timestamp2 = [527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079, 317455832, 411747930]
website2 = ["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi","yljmntrclw","hibympufi", "yljmntrclw"]

print(mostVisitedPattern3(username1, timestamp1, website1))
print(mostVisitedPattern3(username2, timestamp2, website2))