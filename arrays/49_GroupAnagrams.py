#Group Anagrams
from collections import defaultdict
def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        count = tuple(count)
        if count in res:
            res[count].append(s)
        else:
            res[count] = [s]

    return res.values()

def groupAnagrams2(strs):
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(word)
    return groups.values()

def groupAnagrams3(strs):
    anagrams = defaultdict(list)

    for s in strs:
        anagrams[''.join(sorted(s))].append(s)
    
    return list(anagrams.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))