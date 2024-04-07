def characterReplacement(s, k):
    freq = {}
    l, maxF, res = 0, 0, 0
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        maxF = max(freq[s[r]], maxF)
        
        while r - l + 1 - maxF > k:
            freq[s[l]]  -= 1
            l += 1
        
        res = max(res, r - l + 1)
    return res


print(characterReplacement('AABABBA', 1))
print(characterReplacement('ABAB', 2))