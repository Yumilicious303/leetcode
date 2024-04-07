def combine(n, k):
    res = []
    def backtrack(start, curr):
        if len(curr) == k:
            res.append(curr[:])
            return
        
        for num in range(start, n + 1):
            curr.append(num)
            backtrack(num + 1, curr)
            curr.pop()

    backtrack(1, [])
    return res

print(combine(4, 2))
