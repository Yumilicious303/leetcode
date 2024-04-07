def letterCombinations(digits):
    digit_map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    res = []

    def dfs(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for letter in digit_map[int(digits[i])]:
            dfs(i + 1, curr + letter)
    
    dfs(0, '')
    return res


print(letterCombinations("23"))
print(letterCombinations(""))

