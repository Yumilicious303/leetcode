#Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    windowSet = set()
    res = 0
    l = 0
    for r in range(len(s)):
        if s[r] not in windowSet:
            windowSet.add(s[r])
            res = max(res, r - l + 1)
        else:
            while s[l] != s[r]:
                windowSet.remove(s[l])
                l += 1
            l += 1
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

