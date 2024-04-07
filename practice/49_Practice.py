from collections import defaultdict
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[abs(ord('a') - ord(c))] += 1
        anagrams[tuple(count)].append(s)

    return list(anagrams.values())

def groupAnagrams2(strs):
    anagrams = defaultdict(list)

    for s in strs:
        anagrams[''.join(sorted(s))].append(s)
    
    return list(anagrams.values())


print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams2([""]))
print(groupAnagrams2(["a"]))