#Longest Substring Without Repeating Characters
def lengthOfLongestSubstring1(s):
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

def lengthOfLongestSubstring(s):
    windowSet = set()
    l, res = 0, 0
    for r in range(len(s)):
        while s[r] in windowSet:
            windowSet.remove(s[l])
            l += 1
        windowSet.add(s[r])
        res = max(res, len(windowSet))
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

