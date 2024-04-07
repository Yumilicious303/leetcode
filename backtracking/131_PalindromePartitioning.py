#Palindrome Paritioning
def partitionNeet(s):
    res = []
    curr = []

    def backtrack(i):
        if i >= len(s):
            res.append(curr[:])
            return
        
        for j in range(i, len(s)):
            print(s[i:j+1], i,j)
            if isPalindrome(s, i, j):
                curr.append(s[i:j+1])
                backtrack(j + 1)
                curr.pop()
    backtrack(0)
    return res
    


def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

print(partitionNeet("aab"))

