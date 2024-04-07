#Letter Combinations
'''def letterCombinations(digits):
    curr = ''
    res = []
    def backtrack(curr, digitIndex, letterIndex):
        if len(curr) == len(digits):
            res.append(curr[:])
            return
        if letterIndex >= len(digitMap[digits[digitIndex]]):
            return
        
        for digitIndex in range(len(digits)):
            curr = curr + digitMap[digits[digitIndex]][letterIndex]
            backtrack(curr, digitIndex, letterIndex + 1)
            curr = curr[:-1]
            backtrack(curr, digitIndex, letterIndex)

        
    backtrack(curr, 0, 0)
    return res'''

'''def letterCombinations(digits):
    curr = ''
    res = []
    def backtrack(curr, digitIndex, letterIndex):
        if len(curr) == len(digits):
            res.append(curr[:])
            return
        if letterIndex >= len(digitMap[digits[digitIndex]]):
            return
        
        curr = curr + digitMap[digits[digitIndex]][letterIndex]
        backtrack(curr, digitIndex + 1, letterIndex)
        curr = curr[:-1]
        backtrack(curr, digitIndex, letterIndex + 1)

        
    backtrack(curr, 0, 0)
    return res'''

'''def letterCombinations(digits):
    curr = ''
    res = []
    def backtrack(curr, digitIndex, letterIndex):
        if len(curr) == len(digits):
            res.append(curr[:])
            return

        for letterIndex in range(len(digitMap[digits[digitIndex]])):
            curr = curr + digitMap[digits[digitIndex]][letterIndex]
            backtrack(curr, digitIndex + 1, letterIndex)
            curr = curr[:-1]
            backtrack(curr, digitIndex, letterIndex + 1)

    backtrack(curr, 0, 0)
    return res'''

def letterCombinations(digits):
    res = []
    digitMap = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs', 
        '8' : 'tuv',
        '9' : 'wxyz'}

    def backtrack(curr, i):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for c in digitMap[digits[i]]:
            backtrack(curr + c, i + 1)
    if digits:
        backtrack('', 0)
    return res



print(letterCombinations('23'))

        