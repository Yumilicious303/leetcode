#Valid Palindrome
def isPalindrome(s):
    s_alnum = ''

    for char in s:
        if char.isalnum():
            s_alnum += char

    s_alnum = s_alnum.lower()
    l, r = 0, len(s_alnum) - 1
    while r > l:
        if s_alnum[l] != s_alnum[r]:
            return False
        l += 1
        r -= 1
    return True


def isPalindromeNeet(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def isPalindromeNeet2(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


print(isPalindromeNeet2("A man, a plan, a canal: Panama"))
print(isPalindromeNeet2("race a car"))
print(isPalindromeNeet2(" "))