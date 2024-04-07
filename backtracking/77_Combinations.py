#Combinations
def combine(n, k):
    answer = []
    def backtrack(curr, start):
        if len(curr) == k:
            answer.append(curr[:])
            return

        for i in range(start, n + 1):
            curr.append(i)
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 1)
    return answer



print(combine(4, 2))