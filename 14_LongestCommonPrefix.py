#Longest Common Prefix
def longestCommonPrefix(strs):
    res = strs[0]
    for s in strs:
        i, j = 0, 0
        while i < len(res) and j < len(s) and res[i] == s[j]:
            i += 1
            j += 1
        res = res[:i]
    return res

def longestCommonPrefixNeet(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
