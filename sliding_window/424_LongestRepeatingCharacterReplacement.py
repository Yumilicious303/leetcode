#Longest Repeating Character Replacement 
def characterReplacement(s,k): #Initial attempt
    def helper(z):
        currLetter = z[0]
        kCurrent = k
        longest = 0
        beginning = 0
        end = 0
        currLength = 0

        while end < len(z):
            if z[end] == currLetter:
                currLength += 1
                end += 1
            else:
                if kCurrent > 0:
                    currLength += 1
                    kCurrent -= 1
                    end += 1
                else:
                    beginning = end
                    currLength = 0
                    currLetter = z[end]
            longest = max(longest, currLength)
        return longest
    return max(helper(s), helper(s[::-1]))


def characterReplacementNeet(s, k): #After watching Neetcode drawing explanation (no code)
    windowDict = {}
    maxLetterCount = 1
    res = 0
    windowLength = 0
    l, r = 0, 0
    while r < len(s):
        windowLength = r - l + 1
        if windowLength - maxLetterCount <= k:
            #window is valid
            if s[r] not in windowDict:
                windowDict[s[r]] = 1
            else:
                windowDict[s[r]] += 1
            maxLetterCount = max(maxLetterCount, windowDict[s[r]])
            r += 1
            res = max(res, windowLength)
        else:
            #window is invalid
            windowDict[s[l]] -= 1
            l += 1
    return res

def characterReplacementNeet2(s, k): #After watching Neetcode drawing explanation (no code) 2nd attempt
    windowDict = {}
    maxLetterCount = 1
    res = 0
    windowLength = 0
    l, r = 0, 0
    valid = True
    while r < len(s):
        if valid:
            if s[r] not in windowDict:
                windowDict[s[r]] = 1
            else:
                windowDict[s[r]] += 1
            maxLetterCount = max(maxLetterCount, windowDict[s[r]])
        
        windowLength = r - l + 1

        if windowLength - maxLetterCount <= k:
            #window is valid
            r += 1
            res = max(res, windowLength)
        else:
            #window is invalid
            windowDict[s[l]] -= 1
            l += 1
    return res

def characterReplacementNeet3(s,k): #Neetcode's solution in code
    windowDict = {}
    res = 0
    l = 0
    for r in range(len(s)):
        windowDict[s[r]] = windowDict.get(s[r], 0) + 1
        
        while (r - l + 1) - max(windowDict.values())  > k:
            windowDict[s[l]] -= 1
            l += 1
    
        res = max(res, r - l + 1)
    return res

def characterReplacementNeet3WithOptimization(s,k):
    windowDict = {}
    l, maxF, res = 0, 0, 0
    
    for r in range(len(s)):
        windowDict[s[r]] = windowDict.get(s[r], 0) + 1
        maxF = max(maxF, windowDict[s[r]])
        
        while (r - l + 1) - maxF  > k:
            windowDict[s[l]] -= 1
            l += 1
    
        res = max(res, r - l + 1)
    return res

    
print(characterReplacementNeet3WithOptimization("AABABBA", 1))
print(characterReplacementNeet3WithOptimization("ABAB", 2))
print(characterReplacementNeet3WithOptimization("ABAA", 0))
print(characterReplacementNeet3WithOptimization("ABBB", 2))
print(characterReplacementNeet3WithOptimization("BAAAB", 2))