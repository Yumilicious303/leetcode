#Longest Palindrome Substring 
def longestPalindrome(s): 
    def longestPalindromeFromIthPosition(i, j):
        nonlocal res
        while j < len(s) and i >= 0 and s[i] == s[j]:
            if len(res) < j - i + 1:
                res = s[i:j + 1]
            i -= 1
            j += 1

    res = ''
    for i in range(len(s)):
        longestPalindromeFromIthPosition(i, i)
        longestPalindromeFromIthPosition(i, i + 1)
    return res


def longestPalindromeNeet(s: str) -> str:
    res = ""
    resLen = 0
    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res

print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
print(longestPalindrome('aaaa'))
        
        
        
