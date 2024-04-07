#String Permutation 
from collections import Counter
def checkInclusion(s1, s2):
    s1Dict = {}
    s2Dict = {}
    for letter in s1:
        s1Dict[letter] = s1Dict.get(letter, 0) + 1
    l = 0

    for r in range(len(s2)):
        if s2[r] in s1Dict:
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
            if s2Dict[s2[r]] > s1Dict[s2[r]]:
                while s2[l] != s2[r]:
                    s2Dict[s2[l]] -= 1
                    l += 1
                s2Dict[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        else:
            l = r + 1
            s2Dict.clear()
    return False

def checkInclusionComment(s1: str, s2: str) -> bool:
    s1_map = Counter(s1)
    s2_map = Counter()
    if len(s1) > len(s2):
        return False
    
    for i in range(len(s2)):
        s2_map[s2[i]] += 1
        if i >= len(s1):
            if s2_map[s2[i - len(s1)]] > 1:
                s2_map[s2[i - len(s1)]] -= 1                    
            else:
                del s2_map[s2[i - len(s1)]]
        if s1_map == s2_map:
            return True 


        return False


print(checkInclusionComment("ab", "eidbaooo"))
print(checkInclusionComment("ab", "dboaoo"))
print(checkInclusionComment("adc", "dcda"))
