#Palindrome Substrings
def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        j = i
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
    
    for i in range(len(s)):
        j = i + 1
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1

    return count

print(countSubstrings('abc'))
print(countSubstrings('aaa'))
print(countSubstrings('a'))
print(countSubstrings(''))



